from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet, GroupMembershipViewSet, find_matches

router = DefaultRouter()
router.register(r'study-groups', StudyGroupViewSet, basename='studygroup')
router.register(r'memberships', GroupMembershipViewSet, basename='groupmembership')

urlpatterns = [
    path('matches/find/', find_matches, name='find_matches'), # The Matchmaker endpoint
    path('', include(router.urls)),
]
