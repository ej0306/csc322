import datetime
from enum import auto

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.fields import DateTimeField


# Create your models here.
from django.urls import reverse

FIRST = "First"
SECOND = "Second"

SEMESTER = (
    (FIRST, "First"),
    (SECOND, "Second"),
)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_registrar = models.BooleanField(default=False)

    is_suspended = models.BooleanField(default=False)
    suspend_next_sem = models.BooleanField(default=False)
    new_user = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50, default='', blank=True)
    last_name = models.CharField(max_length=50, default='', blank=True)
    m_initial = models.CharField(max_length=1, default='', blank=True)
    email = models.EmailField(max_length=254, default='', unique=True, blank=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date(1, 1, 1), blank=True)
    phone_number = models.IntegerField(default=0, blank=True)
    street_address = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=2, default='', blank=True)
    zip_code = models.IntegerField(default=0, blank=True)

    def __str__(self) -> str:
        return self.last_name + ", " + self.first_name

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk': self.id})

    def get_suspend_url(self):
        return reverse('suspend_user', kwargs={'pk': self.id})

    def get_lift_suspension_url(self):
        return reverse('lift_user_suspension', kwargs={'pk': self.id})

    def get_termination_url(self):
        return reverse('terminate_user', kwargs={'pk': self.id})


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id_number = models.CharField(max_length=20, unique=True, null=True)
    sc_name = models.CharField(max_length=50, null=True)
    sc_city = models.CharField(max_length=50, null=True)
    sc_state = models.CharField(max_length=2, null=True)
    semester = models.CharField(choices=SEMESTER, max_length=50, null=True)
    graduation_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    gpa = models.FloatField(null=True)
    transcript = models.FileField(null=True, blank=True)

    graduation_class = models.ForeignKey("graduation.GraduatingClass", related_name='students', blank=True, null=True, on_delete=models.DO_NOTHING)
    special_registration = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.last_name + ", " + self.user.first_name


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    resume = models.FileField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.last_name + ", " + self.user.first_name


class Registrar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return self.user.last_name + ", " + self.user.first_name


class EnrollmentApplication(models.Model):
    # flags for the type of application
    student_application = models.BooleanField(default=False)
    Instructor_application = models.BooleanField(default=False)

    # personal info
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    m_initial = models.CharField(max_length=1, null=True)
    email = models.EmailField(max_length=254, default='', unique=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date(1, 1, 1))
    phone_number = models.IntegerField(default=0)
    street_address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=2, default='')
    zip_code = models.IntegerField(default=0)

    # previous school & academic info - for students
    sc_name = models.CharField(max_length=50, null=True)
    sc_city = models.CharField(max_length=50, null=True)
    sc_state = models.CharField(max_length=2, null=True)
    graduation_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    gpa = models.FloatField(null=True)
    transcript = models.FileField(null=True, blank=True)

    # professional info - for instructors
    resume = models.FileField(null=True, blank=True)

    # application status
    status_pending = models.BooleanField(default=True)
    status_approved = models.BooleanField(default=False)
    status_rejected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.last_name + ", " + self.first_name


class Reports(models.Model):

    subject = models.CharField(max_length= 100, null=True)
    description = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.subject + f"{ self.description[:50]}..."

    class Meta:
	    verbose_name_plural = 'Reports'