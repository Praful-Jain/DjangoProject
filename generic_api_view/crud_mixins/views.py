from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializers import StudentSerializer


# GENERIC API VIEW AND MODEL MIXIN
class StudentAPIListCreate(GenericAPIView, ListModelMixin, CreateModelMixin):       # PK id not required
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        # The list method uses the queryset attribute to get all Student objects and,
        #  then uses the serializer_class to serialize the Student objects into JSON format.
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        
class StudentAPIRetrieveUpdateDestroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):     # PK id required
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)



# GENERIC API VIEW AND MODEL MIXIN   --> indivudual classes made for each operation
class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        # The list method uses the queryset attribute to get all Student objects and,
        #  then uses the serializer_class to serialize the Student objects into JSON format.
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)