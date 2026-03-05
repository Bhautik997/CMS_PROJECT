from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Student


@login_required
def student_dashboard(request):
    students = Student.objects.all()
    return render(request, "student_dashboard.html", {"students": students})


@login_required
def faculty_dashboard(request):
    return render(request, "faculty_dashboard.html")