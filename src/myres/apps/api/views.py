from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import permissions, mixins, viewsets

from myres.models import User

from .serializers import LoginSerializer, UserProfileSerializer


class LoginView(JSONWebTokenAPIView):
    """
    View to provide JWT login's.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer


class UserProfileView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display User profile.
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.all()
