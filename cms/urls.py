from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name="login"),

    path('student/', views.student_dashboard, name="student_dashboard"),

    path('faculty/', views.faculty_dashboard, name="faculty_dashboard"),

    path('add_attendance/', views.add_attendance, name="add_attendance"),
]