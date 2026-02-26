from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import StudyGroup, GroupMembership
from .serializers import StudyGroupSerializer, GroupMembershipSerializer
from academics.models import Enrollment
from scheduling.models import AvailabilitySlot
from users.models import User

class StudyGroupViewSet(viewsets.ModelViewSet):
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return StudyGroup.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        group = serializer.save()
        GroupMembership.objects.create(user=self.request.user, group=group)

class GroupMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = GroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return GroupMembership.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ==========================================
# THE MATCHMAKER ALGORITHM
# ==========================================
@extend_schema(
    parameters=[
        OpenApiParameter(
            name='course_id',
            description='The ID of the course to find matches for (e.g., 1)',
            required=True,
            type=int
        )
    ]
)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def find_matches(request):
    """
    Finds classmates with overlapping free time.
    """
    course_id = request.query_params.get('course_id')
    me = request.user

    if not course_id:
        return Response({"error": "Please provide a course_id"}, status=status.HTTP_400_BAD_REQUEST)

    my_slots = AvailabilitySlot.objects.filter(user=me)
    if not my_slots.exists():
        return Response({"message": "You need to add availability slots first."}, status=status.HTTP_400_BAD_REQUEST)

    classmates = Enrollment.objects.filter(course_id=course_id).exclude(user=me)
    classmate_ids = classmates.values_list('user_id', flat=True)

    matches = set()

    for uid in classmate_ids:
        their_slots = AvailabilitySlot.objects.filter(user_id=uid)
        for my_slot in my_slots:
            for their_slot in their_slots:
                if my_slot.day_of_week == their_slot.day_of_week:
                    if (my_slot.start_time < their_slot.end_time) and (my_slot.end_time > their_slot.start_time):
                        matches.add(uid)
                        break

    matched_users = User.objects.filter(id__in=matches).values('id', 'username', 'major')
    return Response({"course_id": course_id, "matches": list(matched_users)})