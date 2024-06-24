from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# We can generate auth_token for users via:-
# 1. Admin application
# 2. Using django manage.py command -> python manage.py drf_create_token <username>
# 3. By exposing an API endpoint ->  http POST http://127.0.0.1:8000/gettoken/ username="___" password="___"
# 4. Signals  

# GEEKY SHOWS -> VIDEO NO. 22
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    # To test this use HTTPie command line HTTP client.
    # http http://127.0.0.1:8000/student_api/ 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTcwMTYxLCJpYXQiOjE3MTg5NjcyMjcsImp0aSI6IjhmNDcwNjdkZWRlMjQ0NzM4OTJmNTljMzA2N2FiODcxIiwidXNlcl9pZCI6MX0.r2qCUjVD_eYXpY7HR4IkWkxNMmXlqJEn908jtRRskrU'
    # http -f POST http://127.0.0.1:8000/student_api/ name=Raj roll=109 city=Bangalore 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTcwMTYxLCJpYXQiOjE3MTg5NjcyMjcsImp0aSI6IjhmNDcwNjdkZWRlMjQ0NzM4OTJmNTljMzA2N2FiODcxIiwidXNlcl9pZCI6MX0.r2qCUjVD_eYXpY7HR4IkWkxNMmXlqJEn908jtRRskrU'
    # http PUT http://127.0.0.1:8000/student_api/4/ name=Aaj roll=109 city=Bangalore 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTcwNTYzLCJpYXQiOjE3MTg5NjcyMjcsImp0aSI6IjFkNjFiOTQ2OWM4YzRkODJiZjc2M2M1YTFkODZiMjFlIiwidXNlcl9pZCI6MX0.gR4oSWTrYoJYBBiKnOaAItT7SmTHtYuxbxV57AkQP-E'
    # http DELETE http://127.0.0.1:8000/student_api/4/ 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4OTcwNTYzLCJpYXQiOjE3MTg5NjcyMjcsImp0aSI6IjFkNjFiOTQ2OWM4YzRkODJiZjc2M2M1YTFkODZiMjFlIiwidXNlcl9pZCI6MX0.gR4oSWTrYoJYBBiKnOaAItT7SmTHtYuxbxV57AkQP-E' 
