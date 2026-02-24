from rest_framework import serializers
from .models import StudyGroup, GroupMembership
from users.models import User

class GroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'discord_handle'] # Share Discord handle only inside the group

class StudyGroupSerializer(serializers.ModelSerializer):
    members = GroupMemberSerializer(many=True, read_only=True)

    class Meta:
        model = StudyGroup
        fields = ['id', 'name', 'course', 'created_at', 'members']

class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = ['id', 'user', 'group', 'joined_at']
        read_only_fields = ['user']
