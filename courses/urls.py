
from django.urls import path
from courses.views import   hello, list_courses , view_course
urlpatterns = [
    path('hello',hello ),
    path("",list_courses),
    path("<name>", view_course)
    
]
