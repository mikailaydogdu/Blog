from django.contrib import admin
from .models import CourseOfline, CourseOnline, Work

# Register your models here.

admin.site.register(CourseOnline)
admin.site.register(CourseOfline)
admin.site.register(Work)