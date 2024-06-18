"""
URL configuration for viewsets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from crud_api import views
from rest_framework.routers import DefaultRouter

# In viewsets, we don't need to define/maintain URLs, just make routers and register your class with router.

router = DefaultRouter()  # Creating Router Object
router.register('student_api', views.StudentViewSet, basename='student')  # register your class with router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),   
]
