from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .throttling import MyThrottleClass
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

# GEEKY SHOWS -> VIDEO NO. 25
# THROTTLIING is used to add restrictions to accessing our api
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # throttle_classes = [AnonRateThrottle, MyThrottleClass]

class StudentAPI(views.APIView):
    def get(self,request, pk=None):
        throttle_classes = [ScopedRateThrottle]
        throttle_scope = 'view'
        if pk is None:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        else:
            stu = get_object_or_404(Student, pk=pk)
            serializer = StudentSerializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        student = request.data
        serializer = StudentSerializer(data=student)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        student = request.data
        serializer = StudentSerializer(data=student, id=pk)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Student updated'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk=None):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'msg':'Student deleted successfully'})

