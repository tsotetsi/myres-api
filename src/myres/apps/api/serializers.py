from allauth.account.utils import setup_user_email
from django.utils.translation import ugettext_lazy as _
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from allauth.account.adapter import get_adapter, email_address_exists

from myres.validators import E164Validator
from myres.models import User, Flat, Application, Residence, ResidenceUser, Student, OrganizationResidence, \
                         OrganizationUser, FlatType


class LoginSerializer(JSONWebTokenSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def __init__(self, *args, **kwargs):
        # Skip the direct parent `__init__` as it resets the fields.
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)


class RegisterSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('2', 'Female'),
    )
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=16, validators=[E164Validator])
    email = serializers.EmailField(required=True)
    gender = serializers.ChoiceField(required=True, choices=GENDER_CHOICES)
    password1 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate_email(self, email):
        email = get_adapter().clean_email(email)

        if email and email_address_exists(email):
            raise serializers.ValidationError(_("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return attrs

    def custom_signup(self, request, user):
        user.name = self.validated_data['name']
        user.surname = self.validated_data['surname']
        user.mobile_number = self.validated_data['mobile_number']
        user.gender = self.validated_data['gender']

    def get_cleaned_data(self):
        return {
            'name': self.validated_data.get('name', ''),
            'surname': self.validated_data.get('surname', ''),
            'mobile_number': self.validated_data.get('mobile_number', ''),
            'email': self.validated_data.get('email', ''),
            'password': self.validated_data.get('password1')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname', 'gender', 'mobile_number')
        read_only_fields = ('id',)


class ResidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = ('name', 'email', 'type', 'capacity', 'address', 'phone_number')


class ResidenceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResidenceUser
        fields = ('user', 'residence')


class OrganizationResidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationResidence
        fields = ('organization', 'residence')


class OrganizationUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationUser
        fields = ('user', 'organization')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('user', 'number')


class FlatTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlatType
        fields = ('id', 'name', 'description')


class FlatSerializer(serializers.ModelSerializer):
    residence = ResidenceSerializer(read_only=True)
    type = FlatTypeSerializer(read_only=True)

    class Meta:
        model = Flat
        fields = ('residence', 'number', 'type', 'info', 'type')


class ApplicationSerializer(serializers.Serializer):
    residence = ResidenceSerializer(read_only=True)
    full_name = serializers.ReadOnlyField(source='applicant.user.get_full_name')
    gender = serializers.ReadOnlyField(source='applicant.user.gender')
    residence = serializers.ReadOnlyField(source='applicant.user.__residence')
    flat = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = Application
        fields = ('flat', 'applicant', 'status', 'residence')


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'gender', 'mobile_number')
        read_only_fields = ('email', 'id',)
