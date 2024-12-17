from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Student
from django.contrib import messages
from django.urls import reverse

# Student Registration View
def student_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        course_option = request.POST['course_option']
        date_of_joining = request.POST['date_of_joining']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']

        # Create User
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        Student.objects.create(user=user, phone_number=phone_number, course_option=course_option, date_of_joining=date_of_joining)

        messages.success(request, 'Student registered successfully.')
        return redirect('login')

    return render(request, 'student_register.html')

# Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')

# Admin Dashboard View
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponse("You are not authorized to view this page.")
    return render(request, 'admin_dashboard.html')

# Student Dashboard View
def student_dashboard(request):
    if request.user.is_staff:
        return HttpResponse("You are not authorized to view this page.")
    return render(request, 'student_dashboard.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')
