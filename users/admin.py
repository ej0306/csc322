from django.contrib import admin
from .models import User, Student, Instructor, Registrar

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Registrar)
