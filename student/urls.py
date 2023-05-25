
from django.urls import path 
from student.views import view_student

urlpatterns = [
    path('<name>',view_student )
]
