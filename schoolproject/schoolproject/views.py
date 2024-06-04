from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'index.html')

def about_us(request):
    return HttpResponse("Welcome to Jainam Academy")

def course(request):
    return HttpResponse("ds")

def course_details(request, courseid):
    return HttpResponse(courseid)