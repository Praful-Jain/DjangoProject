from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

# Note:- Take pull of DjangoProject repo and use the "project_env" virtual environment available in the repo to run application. And to debug we can add custom script in launch.json for individual applications within the DjangoProject repo

class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        # id  = request.data.get('id',None)
        id = pk
        if id is not None:
            stu = get_object_or_404(Student, pk=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):    
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        stu = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Student with id={id} complete update successfully'})
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def patch(self, request, pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        stu = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Student with id={id} partial update successfully'})
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk=None, format=None):
        # id = request.data.get('id')
        id = pk
        stu = get_object_or_404(Student, id=id)
        stu.delete()
        return Response({'msg':f'Student with id={id} deleted successfully'})
