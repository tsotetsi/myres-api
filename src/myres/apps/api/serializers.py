from allauth.account.utils import setup_user_email
from allauth.account.adapter import get_adapter, email_address_exists
from django.utils.translation import ugettext_lazy as _
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from .enums import Gender
from .fields import ChoiceField

from myres.validators import E164Validator
from myres.models import User, Flat, Application, Residence, ResidenceUser, Student, OrganizationResidence, \
                         OrganizationUser, FlatType, Organization, ResidenceFlat


class LoginSerializer(JSONWebTokenSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def __init__(self, *args, **kwargs):
        # Skip the direct parent `__init__` as it resets the fields.
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)


class RegisterSerializer(serializers.Serializer):
    residence = serializers.PrimaryKeyRelatedField(queryset=Residence.objects.all())  # TODO: Filter(org) and validate.
    name = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    mobile_number = serializers.CharField(max_length=16, validators=[E164Validator])
    email = serializers.EmailField(required=True)
    gender = ChoiceField(choices=Gender.choices)
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
            'residence': self.validated_data['residence'],
            'name': self.validated_data['name'],
            'surname': self.validated_data['surname'],
            'mobile_number': self.validated_data['mobile_number'],
            'email': self.validated_data['email'],
            'password': self.validated_data['password1']
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])

        # Auth will fail because passwords were not hashed correctly during registration.
        # Login expects hashed passwords to have 'pbkdf2_sha256$30000' prefix.
        user.set_password(self.cleaned_data['password'])
        user.save()

        # Create student-residence-user relationship.
        self.create_student(user=user, residence=self.cleaned_data['residence'])
        return user

    def create_student(self, user: User = None, residence: Residence = None) -> None:
        Student.objects.create(user=user,
                               residence=residence,
                               number=self.extract_student_number(user.email))

    @staticmethod
    def extract_student_number(email: str = '') -> str:
        # Create student number from email address.
        # This assumes the following
        # format: student_number/id@myuniversity.ac.za.
        return email.split('@')[0]


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'surname', 'gender', 'mobile_number')
        read_only_fields = ('id',)


class ResidenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Residence
        fields = ('id', 'name', 'email', 'type', 'capacity', 'address', 'phone_number')


class ResidenceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResidenceUser
        fields = ('user', 'residence')


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        exclude = ('modified',)


class OrganizationResidenceSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    residence = ResidenceSerializer()

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
    residence = serializers.PrimaryKeyRelatedField(queryset=Residence.objects.all())
    full_name = serializers.ReadOnlyField(source='applicant.user.get_full_name')
    gender = serializers.ReadOnlyField(source='applicant.user.gender')
    flat = serializers.PrimaryKeyRelatedField(queryset=Flat.objects.all())  # TODO: Filter flats related to residence.
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), write_only=True)  # TODO: Filter by organization

    class Meta:
        model = Application
        fields = ('flat', 'applicant', 'gender', 'full_name', 'status', 'residence', 'student')

    def validate(self, attrs):
        flat = attrs['flat']
        residence = attrs['residence']
        student = attrs['student']
        if Application.objects.filter(flat=flat, residence=residence, applicant=student).exists():
            raise serializers.ValidationError('You have already made an application for this residence.')
        if not ResidenceFlat.objects.filter(residence=residence, flat=flat).exists():
            raise serializers.ValidationError('The selected flat does not exist for this residence.')
        if not Student.objects.filter(user=self.context['request'].user, residence=residence).exists():
            raise serializers.ValidationError('You are not registered for the selected residence.')
        return attrs

    def create(self, validated_data):
        data = self.context['request'].data
        residence = Residence.objects.get(id=validated_data['residence'].id)
        student = Student.objects.filter(id=data['student'], residence=data['residence']).first()
        application = Application.objects.create(
            flat=self.validated_data['flat'],
            applicant=student,
            residence=residence
        )
        return application


class UserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'surname', 'gender', 'mobile_number')
        read_only_fields = ('email', 'id',)
