# admin.py
from django.contrib import admin
from .models import Position, Staff, Shift, StaffShift, StaffAttendance


class StaffAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'position', 'first_name', 'last_name', 'phone_number', 'hire_date')  # 'positions' o'rniga 'position'
    list_filter = ('position',)


admin.site.register(Position)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Shift)
admin.site.register(StaffShift)
admin.site.register(StaffAttendance)
