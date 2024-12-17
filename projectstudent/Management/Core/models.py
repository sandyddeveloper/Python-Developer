from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    course_option = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.course_option}"
