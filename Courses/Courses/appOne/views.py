from django.shortcuts import render
from appOne.models import Course
# Create your views here.

def index(request):
    return render(request,'appOne/index.html')

def aboutus(request):
    return render(request,'appOne/aboutus.html')

def contact(request):
    return render(request,'appOne/contact.html')

def courses(request):
    course_list = Course.objects.order_by('course_name')
    course_dict = {'courses':course_list}
    return render(request,'appOne/courses.html',context=course_dict)
