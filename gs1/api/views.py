import json, io
from django.http import JsonResponse,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)  # complex data to python_obj
    # json_data = json.dumps(serializer.data)
    # print(json_data)
    # json_data = JSONRenderer().render(serializer.data)        # python_obj to json_data
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)        # json to python
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'res':'Data created'})
        return JsonResponse({'res':'Data not created'})