from django.db import models
from django.conf import settings

class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)  # e.g. "CS101"
    name = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_code}: {self.name}"

class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')  # Prevents a student from joining the same class twice
