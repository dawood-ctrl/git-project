from django.contrib import admin
from .models import students, course

@admin.register(students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Email', 'dob', 'roll_no')
@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('Course_name', 'credits_hours', 'subjects')


