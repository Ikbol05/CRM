# forms.py
from django import forms
from .models import Position, Staff, Shift, StaffShift, StaffAttendance

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['title']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['user', 'position', 'first_name', 'last_name', 'phone_number', 'hire_date']

class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['name', 'start_time', 'end_time']

class StaffShiftForm(forms.ModelForm):
    class Meta:
        model = StaffShift
        fields = ['staff', 'shift', 'date']

class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model = StaffAttendance
        fields = ['staff', 'check_in', 'check_out', 'date', 'is_present']
