import factory

from myres import models


class UserFactory(factory.DjangoModelFactory):

    name = factory.Sequence(lambda n: "Name %03d" % n)
    surname = factory.Sequence(lambda n: "Surname %03d" % n)
    mobile_number = factory.Sequence(lambda n: "+2783123456%d" % n)

    class Meta:
        model = models.User
        django_get_or_create = ('name', 'surname', 'gender', 'mobile_number')


class FlatTypeFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.FlatType


class ResidenceTypeFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ResidenceType


class ResidenceFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Residence


class ResidenceUserFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ResidenceUser


class FlatFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Flat


class ResidenceFlatFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.ResidenceFlat


class StudentFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Student


class ApplicationFactory(factory.DjangoModelFactory):

    class Meta:
        model = models.Application
