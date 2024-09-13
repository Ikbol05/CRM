from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PositionViewSet, StaffViewSet, ShiftViewSet,
    StaffShiftViewSet, StaffAttendanceViewSet
)

router = DefaultRouter()
router.register(r'positions', PositionViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'staff-shifts', StaffShiftViewSet)
router.register(r'staff-attendance', StaffAttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]