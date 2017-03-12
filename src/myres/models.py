from uuid import uuid4

from django.db import models
from authtools.models import AbstractEmailUser
from model_utils import Choices
from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField
from enumfields import EnumField

from .enums import Gender
from .validators import E164Validator


class User(AbstractEmailUser, TimeStampedModel):
    """
    Custom User model for myres app.
    """
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = EnumField(Gender, max_length=12, null=True)
    mobile_number = models.CharField(max_length=16, validators=[E164Validator])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'mobile_number']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return '{} {}'.format(self.surname, self.name)


class FlatType(models.Model):
    """
    Model to store different flat types.

    We need this because, there are various
    flat/room types for each specific university.
    """
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name


class ResidenceType(models.Model):
    """
    Model to specify the type of Residence.

    Examples are Male, Female or Postgraduates etc.
    """
    name = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.name


class OrganizationType(models.Model):
    """
    Model to specify the type of Organization.

    Examples are University, Hostel, Student Accommodation.
    """
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Organization(TimeStampedModel):
    """
    Model to specify an organization.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phone_number = models.CharField(max_length=16, validators=[E164Validator], blank=True, null=True)

    def __str__(self):
        return self.name


class Residence(TimeStampedModel):
    """
    Model to specify a residence.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.ForeignKey(ResidenceType, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=16, validators=[E164Validator], blank=True, null=True)

    def __str__(self):
        return self.name


class OrganizationResidence(TimeStampedModel):
    """
    Model to link Organization with the Residence.
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('organization', 'residence'),)

    def __str__(self):
        return '{} at {}'.format(self.residence.name, self.organization.name)


class OrganizationUser(TimeStampedModel):
    """
    Model to link User with an Organization.
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('organization', 'user'),)

    def __str__(self):
        return '{} at {}'.format(self.user.get_full_name(), self.organization.name)


class ResidenceUser(TimeStampedModel):
    """
    Model to link User with the Residence.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'residence'),)

    def __str__(self):
        return '{} admin at {}'.format(self.user.name, self.residence.name)


class Flat(TimeStampedModel):
    """
    Model to specify a Flat.
    """
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, unique=True)
    type = models.ForeignKey(FlatType, on_delete=models.CASCADE)
    info = models.TextField(verbose_name="Additional [optional] information")

    def __str__(self):
        return '{} at {}'.format(self.number, self.residence.name)


class ResidenceFlat(models.Model):
    """
    Model to represent relationship between Resident and flat.
    """
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('residence', 'flat'),)

    def __str__(self):
        return '{} at {} resident'.format(self.flat.number, self.residence.name)


class Student(TimeStampedModel):
    """
    Model to specify a Student.

    Students will be distinguished based on their student numbers
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(verbose_name="Student Number", max_length=54)

    def __str__(self):
        return self.number


class Application(TimeStampedModel):
    """
    Model to specify an Application to a Residence.
    """
    STATUS = Choices("NEW", "REVIEW", "APPROVED", "DECLINED", "DELETED")

    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    applicant = models.OneToOneField(Student)
    status = StatusField(default=STATUS.NEW)
    residence = models.ManyToManyField(Residence)

    class Meta:
        ordering = ['created', 'flat', 'status']
        get_latest_by = 'created'

    def __str__(self):
        return '{} {}'.format(self.flat.number, self.applicant.user.name)
