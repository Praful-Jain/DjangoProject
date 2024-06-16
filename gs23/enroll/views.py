from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.
def studentinfo(request):
    obj = Student.objects.all()
    return render(request, "enroll/studetails.html", {'stu':obj})
    # return HttpResponse(obj)