from django.contrib import admin
from django.db import models
from courses.models import CarryOverStudent, Course, Classes, RepeatingStudent, Result, ReviewClasses, Session, TakenCourse, CourseAllocation, WaitList, WarningCount

# Register your models here.
#class CityAdmin(admin.ModelAdmin):
    #list_display = ("name", "state",)

class CourseAdmin (admin.ModelAdmin):
    list_display = ("course_name" , "title",)

class CourseAllocationAdmin (admin.ModelAdmin):
    list_display = ("instructor" ,)

class ScoreAdmin(admin.ModelAdmin):
	list_display = ['student', 'classes', 'ca', 'exam', 'total', 'grade', 'comment']

class ClassesAdmin(admin.ModelAdmin):
	list_display = ['course', 'semester', 'start_date', 'end_date', 'instructor', 'days','start_time', 'end_time']


class ReviewAdmin(admin.ModelAdmin):
    model = ReviewClasses
    list_display = ('course', 'rate', 'date_added', 'owner', 'review')
    list_filter = ['date_added', 'owner']
    search_fields = ['review']

class WarningAdmin(admin.ModelAdmin):
    models = WarningCount
    list_display = ('student', 'count')

admin.site.register(Course, CourseAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(TakenCourse, ScoreAdmin)
admin.site.register(CourseAllocation, CourseAllocationAdmin)
admin.site.register(Session)
admin.site.register(Result)
admin.site.register(CarryOverStudent)
admin.site.register(RepeatingStudent)
admin.site.register(WaitList)


admin.site.register(WarningCount, WarningAdmin)
admin.site.register(ReviewClasses, ReviewAdmin)
