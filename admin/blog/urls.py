# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Register
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Position
    path('positions/', views.position_list, name='position_list'),
    path('positions/<int:pk>/', views.position_detail, name='position_detail'),
    path('positions/create/', views.position_create, name='position_create'),
    path('positions/edit/<int:pk>/', views.position_update, name='position_update'),
    path('positions/delete/<int:pk>/', views.position_delete, name='position_delete'),

    # Staff
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/edit/', views.staff_update, name='staff_update'),
    path('staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    # Shift
    path('shift/', views.shift_list, name='shift_list'),
    path('shift/<int:pk>/', views.shift_detail, name='shift_detail'),
    path('shift/create/', views.shift_create, name='shift_create'),
    path('shift/<int:pk>/edit/', views.shift_update, name='shift_update'),
    path('shift/<int:pk>/delete/', views.shift_delete, name='shift_delete'),

    # StaffShift
    path('staff_shifts/', views.staff_shift_list, name='staff_shift_list'),
    path('staff_shifts/<int:pk>/', views.staff_shift_detail, name='staff_shift_detail'),
    path('staff_shifts/create/', views.staff_shift_create, name='staff_shift_create'),
    path('staff_shifts/<int:pk>/edit/', views.staff_shift_update, name='staff_shift_update'),
    path('staff_shifts/<int:pk>/delete/', views.staff_shift_delete, name='staff_shift_delete'),

    # StaffAttendance
    path('staff_attendances/', views.staff_attendance_list, name='staff_attendance_list'),
    path('staff_attendances/<int:pk>/', views.staff_attendance_detail, name='staff_attendance_detail'),
    path('staff_attendances/create/', views.staff_attendance_create, name='staff_attendance_create'),
    path('staff_attendances/<int:pk>/edit/', views.staff_attendance_update, name='staff_attendance_update'),
    path('staff_attendances/<int:pk>/delete/', views.staff_attendance_delete, name='staff_attendance_delete'),

    # Search
    path('search/', views.search_view, name='search_view')
]

