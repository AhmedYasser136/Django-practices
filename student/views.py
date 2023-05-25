from django.shortcuts import render
# Create your views here.


def view_student(request, name):
    context = {
        "stu_name": name
    }
    return render(request, "index.html", context)
