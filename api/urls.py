from django.contrib import admin
from django.urls import path, include
from .views import student_list, StudentDetail, ViewSet_Enrollment, CourseList, CourseDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('enrollment',ViewSet_Enrollment)


urlpatterns = [
    path('students/list_students/',student_list),
    path('students/<int:pk>/',StudentDetail.as_view()),
    path('course/list_courses/',CourseList.as_view()),
    path('course/<int:pk>/',CourseDetail.as_view()),
    path('',include(router.urls)),
]
