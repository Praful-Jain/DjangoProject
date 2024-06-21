from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    # To test this use HTTPie command line HTTP client.