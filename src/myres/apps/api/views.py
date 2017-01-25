from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import permissions, mixins, viewsets

from myres.models import User, Residence, Student

from .serializers import LoginSerializer, UserProfileSerializer, ResidenceSerializer, StudentSerializer,\
                         ApplicationSerializer, FlatSerializer


class LoginView(JSONWebTokenAPIView):
    """
    View to provide JWT login's.
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer


class UserView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display User profile.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return User.objects.all()


class ResidenceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Residence.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ResidenceSerializer

    def get_queryset(self):
        return Residence.objects.all()


class StudentView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Student.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()


class ApplicationView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Applications.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ApplicationSerializer


class FlatView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Flats.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = FlatSerializer
