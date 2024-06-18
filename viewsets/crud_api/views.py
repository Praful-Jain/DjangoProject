from django.shortcuts import render, get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

# viewsets is a module in Django Rest Framework (DRF) that provides a set of classes to help create views that combine the logic for handling multiple HTTP methods (GET, POST, PUT, DELETE, etc.) into a single class.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Added student'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Updated student with id={pk}'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':f'Partially updated student with id={pk}'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        stu = get_object_or_404(Student, id=pk)
        stu.delete()
        return Response({'msg':f'Student with id={pk} deleted successfully'})


# The ModelViewSet class inherits from GenericAPIView and includes implementation for various actions, by mixing in the behavior of the various mixin classes
# Provides list(), retrieve(), create(), update(), partial_update() and destroy() actions.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer