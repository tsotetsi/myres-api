from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework import serializers

from myres.models import User


class LoginSerializer(JSONWebTokenSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        # Skip the direct parent `__init__` as it resets the fields.
        super(JSONWebTokenSerializer, self).__init__(*args, **kwargs)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
