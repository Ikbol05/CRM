import os
import django
import random
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker
from blog.models import Position, Staff, Shift, StaffShift, StaffAttendance

fake = Faker()


def create_positions():
    positions = ['Manager', 'Assistant Manager', 'Cashier', 'Sales Associate', 'Customer Service Representative']
    for title in positions:
        Position.objects.get_or_create(title=title)


def create_users_and_staff(num_staff):
    positions = list(Position.objects.all())
    for _ in range(num_staff):
        username = fake.user_name()
        email = fake.email()
        password = 'password123'  # You might want to generate random passwords
        user = User.objects.create_user(username=username, email=email, password=password)

        Staff.objects.create(
            user=user,
            position=random.choice(positions),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            phone_number=fake.phone_number(),
            hire_date=fake.date_between(start_date='-5y', end_date='today')
        )


def create_shifts():
    shifts = [
        ('Morning', '08:00', '16:00'),
        ('Afternoon', '16:00', '00:00'),
        ('Night', '00:00', '08:00')
    ]
    for name, start, end in shifts:
        Shift.objects.get_or_create(name=name, start_time=start, end_time=end)


def create_staff_shifts(num_days):
    staff = list(Staff.objects.all())
    shifts = list(Shift.objects.all())
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=num_days)

    for staff_member in staff:
        current_date = start_date
        while current_date <= end_date:
            if random.choice([True, False]):  # 50% chance of having a shift
                StaffShift.objects.create(
                    staff=staff_member,
                    shift=random.choice(shifts),
                    date=current_date
                )
            current_date += timedelta(days=1)


def create_staff_attendance(num_days):
    staff = list(Staff.objects.all())
    end_date = timezone.now().date()
    start_date = end_date - timedelta(days=num_days)

    for staff_member in staff:
        current_date = start_date
        while current_date <= end_date:
            if random.choice([True, False, False]):  # 33% chance of being absent
                check_in = timezone.make_aware(fake.date_time_between(
                    start_date=f'{current_date} 07:00:00',
                    end_date=f'{current_date} 10:00:00'
                ))
                check_out = check_in + timedelta(hours=random.randint(7, 9))
                StaffAttendance.objects.create(
                    staff=staff_member,
                    check_in=check_in,
                    check_out=check_out,
                    date=current_date,
                    is_present=True
                )
            else:
                StaffAttendance.objects.create(
                    staff=staff_member,
                    date=current_date,
                    is_present=False
                )
            current_date += timedelta(days=1)


if __name__ == '__main__':
    print('Populating database...')
    create_positions()
    create_users_and_staff(num_staff=20)
    create_shifts()
    create_staff_shifts(num_days=30)
    create_staff_attendance(num_days=30)
    print('Database population completed.')