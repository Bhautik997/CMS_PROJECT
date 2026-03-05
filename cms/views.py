from django.shortcuts import render
from .models import Student


def login_view(request):
    return render(request, "login.html")


def student_dashboard(request):
    students = Student.objects.all()
    return render(request, "student_dashboard.html", {"students": students})


def faculty_dashboard(request):
    return render(request, "faculty_dashboard.html")