import os
import django
from datetime import time

# 1. Setup the Django environment so the script can talk to your database
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studysquad_core.settings')
django.setup()

# Import your custom models
from users.models import User
from academics.models import Course, Enrollment
from scheduling.models import AvailabilitySlot

def create_dummy_data():
    print("🛠️ Starting data generation...")

    # 2. Create a Course (using get_or_create so it doesn't duplicate if run twice)
    course, _ = Course.objects.get_or_create(
        course_code='CS101',
        defaults={'name': 'Intro to Python', 'instructor': 'Dr. Smith'}
    )
    print(f"📚 Course ready: {course.course_code}")

    # 3. Create Users
    sarah, _ = User.objects.get_or_create(username='Sarah', defaults={'email': 'sarah@example.com', 'major': 'Computer Science'})
    sarah.set_password('password123')
    sarah.save()

    john, _ = User.objects.get_or_create(username='John', defaults={'email': 'john@example.com', 'major': 'Mathematics'})
    john.set_password('password123')
    john.save()

    lionel, _ = User.objects.get_or_create(username='Lionel', defaults={'email': 'lionel@example.com', 'major': 'Backend Engineering'})
    lionel.set_password('password123')
    lionel.save()
    print("👥 Users ready: Sarah, John, and Lionel")

    # 4. Enroll Users in the Course
    Enrollment.objects.get_or_create(user=sarah, course=course)
    Enrollment.objects.get_or_create(user=john, course=course)
    Enrollment.objects.get_or_create(user=lionel, course=course)
    print("🎓 Enrollments ready!")

    # 5. Create Availability Slots (The Overlap: Monday between 1PM and 4PM)
    # Sarah is free 2:00 PM to 4:00 PM
    AvailabilitySlot.objects.get_or_create(
        user=sarah, day_of_week='MON', start_time=time(14, 0), end_time=time(16, 0)
    )
    # John is free 2:30 PM to 3:30 PM
    AvailabilitySlot.objects.get_or_create(
        user=john, day_of_week='MON', start_time=time(14, 30), end_time=time(15, 30)
    )
    # Lionel is free 1:00 PM to 3:00 PM (This perfectly overlaps with both of them!)
    AvailabilitySlot.objects.get_or_create(
        user=lionel, day_of_week='MON', start_time=time(13, 0), end_time=time(15, 0)
    )
    print("📅 Schedules ready!")
    
    print("\n✅ All dummy data created successfully! The Matchmaker is primed.")

if __name__ == '__main__':
    create_dummy_data()