from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custom_permission import MyPermission
from .custom_authentication import MyAuthentication

# Authentication -> BasicAuthentication, SessionAuthentication, TokenAuthentication, CustomAuthentication
# There also exist some third-party packages which provides permissions :-
# 1. DRF - Access Policy
# 2. Composed permissions
# 3. REST Condition
# 4. DRY Rest permissions
# 5. Django Rest Framework Roles
# 6. DRF API key
# 7. DRF Role Filters
# 8. DRF PSQ

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication]
    authentication_classes = [MyAuthentication]     # Custom authentication

    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAdminUser]
    # permission_classes = [DjangoModelPermissions]       
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]       
    permission_classes = [IsAuthenticated]         # Custom permission

    # "DjangoModelPermission" must only only be applied to view-classes having queryset property or get_queryset(), and we need to give particular permissions to users manually to make changes in the models
    # ie...   POST -> add permission
    #         PUT, PATCH -> change permission
    #         DELETE -> delete permisssion
