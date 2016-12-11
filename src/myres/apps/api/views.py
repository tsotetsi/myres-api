from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import permissions

from .serializers import LoginSerializer


class LoginView(JSONWebTokenAPIView):
    """
    View to provide JWT logins.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer
