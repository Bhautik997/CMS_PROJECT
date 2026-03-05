from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('student/', views.student_dashboard, name="student_dashboard"),
    path('faculty/', views.faculty_dashboard, name="faculty_dashboard"),
]