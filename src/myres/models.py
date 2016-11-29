from uuid import uuid4

from django.db import models
from django.contrib.sites.models import Site
from authtools.models import AbstractEmailUser
from model_utils.models import TimeStampedModel
from enumfields import EnumField

from .enums import Gender
from .validators import E164Validator


class User(AbstractEmailUser, TimeStampedModel):
    """
    Custom User model for myres.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = EnumField(Gender, max_length=12, null=True)
    mobile_number = models.CharField(max_length=16, validators=[E164Validator])

    REQUIRED_FIELDS = ['name', 'surname', 'mobile_number']

    def __str__(self):
        return self.email
