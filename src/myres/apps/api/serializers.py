from allauth.account.utils import setup_user_email
from django.utils.translation import ugettext_lazy as _
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from allauth.account.adapter import get_adapter, email_address_exists

from myres.validators import E164Validator
from myres.models import User, Flat, Application, Residence, ResidenceUser, Student


class LoginSerializer(JSONWebTokenSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        # Skip the direct parent `__init__` as it resets the fields.
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)


class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=16, validators=[E164Validator])
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)

        if email and email_address_exists(email):
            raise serializers.ValidationError(_("A user is already registered with this e-mail address."))
        return email

    def validate_password(self, password):
        return get_adapter().clean_password(password)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return attrs

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'surname': self.validated_data.get('surname', ''),
            'mobile_number': self.validated_data.get('mobile_number', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user


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

