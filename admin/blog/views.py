from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from .models import Position, Staff, Shift, StaffShift, StaffAttendance
from .forms import PositionForm, StaffForm, ShiftForm, StaffShiftForm, \
    StaffAttendanceForm


def is_admin(user):
    return user.is_authenticated and user.is_staff


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper


@login_required(login_url='login')
@admin_required
def index(request):
    return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'registration/register.html',
                              {'error': 'Bu foydalanuvchi nomi allaqachon mavjud'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'registration/register.html',
                              {'error': 'Bu elektron pochta allaqachon ro\'yxatdan o\'tgan'})
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                return redirect('index')
        else:
            return render(request, 'register.html', {'error': 'Parollar mos kelmadi'})
    return render(request, 'registration/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Noto\'g\'ri foydalanuvchi nomi yoki parol'})
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


# Position Views
@login_required(login_url='login')
@admin_required
def position_list(request):
    positions = Position.objects.all()
    return render(request, 'positions/position_list.html', {'positions': positions})


@login_required(login_url='login')
@admin_required
def position_detail(request, pk):
    position = get_object_or_404(Position, pk=pk)
    return render(request, 'positions/position_detail.html', {'position': position})


@login_required(login_url='login')
@admin_required
def position_create(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('position_list')
    else:
        form = PositionForm()
    return render(request, 'positions/position_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def position_update(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        form = PositionForm(request.POST, instance=position)
        if form.is_valid():
            form.save()
            return redirect('position_detail', pk=pk)
    else:
        form = PositionForm(instance=position)
    return render(request, 'positions/position_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def position_delete(request, pk):
    position = get_object_or_404(Position, pk=pk)
    if request.method == 'POST':
        position.delete()
        return redirect('position_list')
    return render(request, 'positions/position_confirm_delete.html', {'position': position})


@login_required(login_url='login')
@admin_required
# Staff Views
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'Staff/staff_list.html', {'staff': staff})


@login_required(login_url='login')
@admin_required
def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'Staff/staff_detail.html', {'staff': staff})


@login_required(login_url='login')
@admin_required
def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'Staff/staff_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_detail', pk=pk)
    else:
        form = StaffForm(instance=staff)
    return render(request, 'Staff/staff_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'Staff/staff_confirm_delete.html', {'staff': staff})


@login_required(login_url='login')
@admin_required
# Shift Views
def shift_list(request):
    shifts = Shift.objects.all()
    return render(request, 'shift/shift_list.html', {'shifts': shifts})


@login_required(login_url='login')
@admin_required
def shift_detail(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    return render(request, 'shift/shift_detail.html', {'shift': shift})


@login_required(login_url='login')
@admin_required
def shift_create(request):
    if request.method == 'POST':
        form = ShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shift_list')
    else:
        form = ShiftForm()
    return render(request, 'shift/shift_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def shift_update(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return redirect('shift_detail', pk=pk)
    else:
        form = ShiftForm(instance=shift)
    return render(request, 'shift/shift_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def shift_delete(request, pk):
    shift = get_object_or_404(Shift, pk=pk)
    if request.method == 'POST':
        shift.delete()
        return redirect('shift_list')
    return render(request, 'shift/shift_confirm_delete.html', {'shift': shift})


@login_required(login_url='login')
@admin_required
# StaffShift Views
def staff_shift_list(request):
    staff_shifts = StaffShift.objects.all()
    return render(request, 'staffShift/staff_shift_list.html', {'staff_shifts': staff_shifts})


@login_required(login_url='login')
@admin_required
def staff_shift_detail(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    return render(request, 'staffShift/staff_shift_detail.html', {'staff_shift': staff_shift})


@login_required(login_url='login')
@admin_required
def staff_shift_create(request):
    if request.method == 'POST':
        form = StaffShiftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_shift_list')
    else:
        form = StaffShiftForm()
    return render(request, 'staffShift/staff_shift_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_shift_update(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        form = StaffShiftForm(request.POST, instance=staff_shift)
        if form.is_valid():
            form.save()
            return redirect('staff_shift_detail', pk=pk)
    else:
        form = StaffShiftForm(instance=staff_shift)
    return render(request, 'staffShift/staff_shift_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_shift_delete(request, pk):
    staff_shift = get_object_or_404(StaffShift, pk=pk)
    if request.method == 'POST':
        staff_shift.delete()
        return redirect('staff_shift_list')
    return render(request, 'staffShift/staff_shift_confirm_delete.html', {'staff_shift': staff_shift})


# StaffAttendance Views
@login_required(login_url='login')
@admin_required
def staff_attendance_list(request):
    attendances = StaffAttendance.objects.all()
    return render(request, 'StaffAttendance/staff_attendance_list.html', {'attendances': attendances})


@login_required(login_url='login')
@admin_required
def staff_attendance_detail(request, pk):
    attendance = get_object_or_404(StaffAttendance, pk=pk)
    return render(request, 'StaffAttendance/staff_attendance_detail.html', {'attendance': attendance})


@login_required(login_url='login')
@admin_required
def staff_attendance_create(request):
    if request.method == 'POST':
        form = StaffAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_attendance_list')
    else:
        form = StaffAttendanceForm()
    return render(request, 'StaffAttendance/staff_attendance_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_attendance_update(request, pk):
    attendance = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        form = StaffAttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('staff_attendance_detail', pk=pk)
    else:
        form = StaffAttendanceForm(instance=attendance)
    return render(request, 'StaffAttendance/staff_attendance_form.html', {'form': form})


@login_required(login_url='login')
@admin_required
def staff_attendance_delete(request, pk):
    attendance = get_object_or_404(StaffAttendance, pk=pk)
    if request.method == 'POST':
        attendance.delete()
        return redirect('staff_attendance_list')
    return render(request, 'StaffAttendance/staff_attendance_confirm_delete.html', {'attendance': attendance})


def search_view(request):
    query = request.GET.get('q')
    if query:
        results = StaffAttendance.objects.filter(
            Q(staff__first_name__icontains=query) |
            Q(staff__last_name__icontains=query) |
            Q(date__icontains=query) |
            Q(is_present__icontains=query)
        )
    else:
        results = StaffAttendance.objects.all()

    context = {
        'results': results,
        'query': query,
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string('StaffAttendance/search_results_partial.html', context)
        return JsonResponse({'html': html})

    return render(request, 'search_results.html', context)