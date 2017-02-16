from factory import DjangoModelFactory, SubFactory

from myres import models


class UserFactory(DjangoModelFactory):

    class Meta:
        model = models.User


class FlatTypeFactory(DjangoModelFactory):

    class Meta:
        model = models.FlatType


class ResidenceTypeFactory(DjangoModelFactory):

    class Meta:
        model = models.ResidenceType


class ResidenceFactory(DjangoModelFactory):

    class Meta:
        model = models.Residence


class ResidenceUserFactory(DjangoModelFactory):

    class Meta:
        model = models.ResidenceUser


class FlatFactory(DjangoModelFactory):

    class Meta:
        model = models.Flat


class ResidenceFlatFactory(DjangoModelFactory):

    class Meta:
        model = models.ResidenceFlat


class StudentFactory(DjangoModelFactory):

    class Meta:
        model = models.Student


class ApplicationFactory(DjangoModelFactory):

    class Meta:
        model = models.Application
