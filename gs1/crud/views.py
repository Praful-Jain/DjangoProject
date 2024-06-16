import json,io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Added student'})
        return JsonResponse({'msg':serializer.errors})
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            id = python_data.get('id')
            instance = Student.objects.get(id=id)
            serializer = StudentSerializer(instance, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'Student updated'})
            return JsonResponse({'msg':serializer.error})
        except Exception as e:
            return JsonResponse({'msg':str(e)})
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        try:
            if id is not None:
                # record = get_object_or_404(Student, id=id)
                record = Student.objects.get(id=id)
                record.delete()
                return JsonResponse({'msg': f'Record with id: {id} deleted sucessfully'})
            else:
                Student.objects.all().delete()
                return JsonResponse({'msg': 'All records deleted'})
        except Http404:
            return JsonResponse({'msg':'Record not found'})
        except Exception as e:
            return JsonResponse({'msg':str(e)})

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg':'Added student'})
        return JsonResponse({'msg':serializer.errors})
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        try:
            id = python_data.get('id')
            instance = Student.objects.get(id=id)
            serializer = StudentSerializer(instance, data=python_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'msg':'Student updated'})
            return JsonResponse({'msg':serializer.error})
        except Exception as e:
            return JsonResponse({'msg':str(e)})
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        try:
            if id is not None:
                # record = get_object_or_404(Student, id=id)
                record = Student.objects.get(id=id)
                record.delete()
                return JsonResponse({'msg': f'Record with id: {id} deleted sucessfully'})
            else:
                Student.objects.all().delete()
                return JsonResponse({'msg': 'All records deleted'})
        except Http404:
            return JsonResponse({'msg':'Record not found'})
        except Exception as e:
            return JsonResponse({'msg':str(e)})
