from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework import permissions, mixins, viewsets

from myres.models import User, Residence, Student, Application, Flat, OrganizationResidence, OrganizationUser

from .serializers import LoginSerializer, UserProfileSerializer, ResidenceSerializer, StudentSerializer, \
                         ApplicationSerializer, FlatSerializer, OrganizationResidenceSerializer, \
                         OrganizationUserSerializer


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


class OrganizationUserView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Organization Users.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = OrganizationUserSerializer

    def get_queryset(self):
        organization = self.request.query_params.get('organization', None)
        return OrganizationUser.objects.filter(organization=organization)


class OrganizationResidenceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Organization Residence.
    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OrganizationResidenceSerializer

    def get_queryset(self):
        residence = self.request.query_params.get('residence', None)
        return OrganizationResidence.objects.filter(residence=residence)


class ResidenceView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Residence.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ResidenceSerializer

    def get_queryset(self):
        residence = self.request.query_params.get('residence', None)
        return Residence.objects.filter(id=residence)


class StudentView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Student.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = StudentSerializer

    def get_queryset(self):
        student_number = self.request.query_params.get('student_number', None)
        return Student.objects.filter(number=student_number)


class ApplicationView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    View to display Applications.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        residence = self.request.query_params.get('residence', None)
        return Application.objects.filter(residence=residence)


class FlatView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    View to display Flats.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = FlatSerializer

    def get_queryset(self):
        residence = self.request.query_params.get('residence', None)
        return Flat.objects.filter(residence=residence)
