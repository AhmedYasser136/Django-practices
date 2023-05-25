from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("hello")


def list_courses(request):
    courses = ["c", "c++", "py"]
    context = {
        "course_list": courses
    }
    return render(request, "courses_index.html", context)


def view_course(request, name):
    context = {
        "course_name" : name 
    }
    return render(request, "view_course.html",context)
