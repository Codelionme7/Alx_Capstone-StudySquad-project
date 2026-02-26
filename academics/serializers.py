from rest_framework import serializers
from .models import Course, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_code', 'name', 'instructor']

class EnrollmentSerializer(serializers.ModelSerializer):
    # This reads the details of the course instead of just the ID
    course_details = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'course_details', 'created_at']
        read_only_fields = ['user', 'created_at']