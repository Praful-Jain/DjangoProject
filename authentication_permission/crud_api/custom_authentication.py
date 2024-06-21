
from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication

class MyAuthentication(BaseAuthentication):
    def authenticate(self,request):
        username = request.GET.get('username',None)
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return AuthenticationFailed('No such user')
        return (user,None)