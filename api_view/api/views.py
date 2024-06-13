from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

#  api_view decorator is part of DRF and is used to turn a function-based view into an API view that can handle specific HTTP methods.
@api_view(['GET','POST'])
def student_api(request):
    if request.method == 'GET':
        qp = request.query_params
        return Response({'msg':F'this is get request {qp}'})
    if request.method == 'POST':
        data = request.data
        return Response({'msg': F'this is post request {data}'})
