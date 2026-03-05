from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Student, Faculty, Attendance, Marks, Fees   
def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        print("Authenticated user:", user)

        if user is not None:

            print("Student exists:", Student.objects.filter(user=user).exists())
            print("Faculty exists:", Faculty.objects.filter(user=user).exists())

            login(request, user)

            if Student.objects.filter(user=user).exists():
                return redirect('student_dashboard')

            if Faculty.objects.filter(user=user).exists():
                return redirect('faculty_dashboard')

        else:
            return render(request, "login.html", {"error": "Invalid login"})

    return render(request, "login.html")
def student_dashboard(request):

    student = Student.objects.get(user=request.user)

    attendance = Attendance.objects.filter(student=student)
    marks = Marks.objects.filter(student=student)
    fees = Fees.objects.filter(student=student)

    context = {
        "attendance": attendance,
        "marks": marks,
        "fees": fees
    }

    return render(request, "student_dashboard.html", context)

def faculty_dashboard(request):

    students = Student.objects.all()

    return render(request, "faculty_dashboard.html", {"students": students})



def add_attendance(request):

    if request.method == "POST":

        student_id = request.POST['student']
        date = request.POST['date']
        status = request.POST['status']

        student = Student.objects.get(id=student_id)

        Attendance.objects.create(
            student=student,
            date=date,
            status=status
        )

        return redirect('faculty_dashboard')

    students = Student.objects.all()

    return render(request, "add_attendance.html", {"students": students})