from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from courses.models import *

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title


# Create your models here.
# class CourseGen(models.Model):
#     course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE  )