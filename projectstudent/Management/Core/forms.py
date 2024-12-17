from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    course_list = forms.CharField(max_length=200)
    date_of_joining = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'course_list', 'date_of_joining']

    # Custom save method to create student profile after user creation
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.is_student = True  # Automatically set the user as a student
            user.save()
            # Create student profile (you can modify this logic if you need additional fields)
            student = Student.objects.create(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                course_list=self.cleaned_data['course_list'],
                date_of_joining=self.cleaned_data['date_of_joining']
            )
            student.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
