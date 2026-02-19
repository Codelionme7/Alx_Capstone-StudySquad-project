from rest_framework import viewsets, permissions
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users to enroll in courses.
    """
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users only see their own enrollments
        return Enrollment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user to the currently logged-in user
        serializer.save(user=self.request.user)
