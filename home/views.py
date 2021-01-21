from django.shortcuts import render
from .models import CourseOnline, CourseOfline, Work

# Create your views here.

def home(request):
    course_online = CourseOnline.objects.all()
    course_ofline = CourseOfline.objects.all()
    work = Work.objects.all()

    context={
        'course_online': course_online,
        'course_ofline': course_ofline,
        'work': work,
    }
    return render(request, 'home.html', context)