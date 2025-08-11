from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    output = " , ".join([s.name for s in students])
    RuntimeError
    return HttpResponse(f"Students: {output}")