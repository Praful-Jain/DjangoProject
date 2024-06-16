from django.urls import path
from . import views

urlpatterns = [
    path('show_info/', views.studentinfo),
]