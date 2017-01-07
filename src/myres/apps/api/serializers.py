from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from myres.validators import E164Validator
from myres.models import User, Flat, Application, Residence, ResidenceUser, Student


class LoginSerializer(JSONWebTokenSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        # Skip the direct parent `__init__` as it resets the fields.
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)


class RegistrationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=16, validators=[E164Validator])
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'gender', 'mobile_number')


class ResidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = ('name', 'email', 'type', 'capacity', 'address', 'phone_number')


class ResidenceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResidenceUser
        fields = ('user', 'residence')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('user', 'number')


class FlatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flat
        fields = ('residence', 'number', 'type', 'info')


class ApplicationSerializer(serializers.Serializer):

    class Meta:
        model = Application
        fields = ('flat', 'applicant', 'status', 'residence')

