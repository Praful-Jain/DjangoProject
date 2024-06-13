from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
@api_view(['GET','POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # id  = request.data.get('id',None)
        id = pk
        if id is not None:
            stu = get_object_or_404(Student, pk=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method =='POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method =='PUT':
        id = request.data.get('id')
        stu = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Student with id={id} complete update successfully'})
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    if request.method =='PATCH':
        id = request.data.get('id')
        stu = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Student with id={id} partial update successfully'})
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    if request.method =='DELETE':
        # id = request.data.get('id')
        id = pk
        stu = get_object_or_404(Student, id=id)
        stu.delete()
        return Response({'msg':f'Student with id={id} deleted successfully'})
