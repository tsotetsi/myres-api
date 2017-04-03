import factory, factory.fuzzy
from faker import Factory as FakerFactory
from random import random

from django.contrib.auth.hashers import make_password

from myres import models

faker = FakerFactory.create()


class UserFactory(factory.DjangoModelFactory):

    name = factory.Sequence(lambda n: "Name %d" % n)
    surname = factory.Sequence(lambda n: "Surname %d" % n)
    mobile_number = factory.Sequence(lambda n: "+2783000000%d" % n)
    email = factory.LazyAttribute(lambda o: '%s@university.ac.za' % o.name)
    gender = random.choices['MALE', 'FEMALE']
    _PASSWORD = 'pass1@Capital'
    password = make_password(_PASSWORD)

    class Meta:
        model = models.User
        django_get_or_create = ('email',)


class FlatTypeFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Flat type %d" % n)
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))

    class Meta:
        model = models.FlatType


class ResidenceTypeFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Residence type %d" % n)
    description = factory.LazyAttribute(lambda x: faker.sentence(nb_words=6))

    class Meta:
        model = models.ResidenceType


class ResidenceFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Residence %d" % n)
    email = factory.LazyAttribute(lambda o: '%s@university.ac.za' % o.name.strip(''))
    type = factory.SubFactory(ResidenceTypeFactory)
    capacity = factory.fuzzy.FuzzyInteger(100, 400)
    address = faker('address')
    phone_number = factory.Sequence(lambda n: "+2721000000%d" % n)

    class Meta:
        model = models.Residence


class ResidenceUserFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    residence = factory.SubFactory(ResidenceFactory)

    class Meta:
        model = models.ResidenceUser


class FlatFactory(factory.DjangoModelFactory):
    residence = factory.SubFactory(ResidenceFlatFactory)
    number = factory.sequence(lambda s: "10%dA" % s)
    type = factory.SubFactory(FlatTypeFactory)
    info = factory.LazyAttribute(lambda s: faker.sentence(nb_words=6))

    class Meta:
        model = models.Flat


class ResidenceFlatFactory(factory.DjangoModelFactory):
    residence = factory.SubFactory(ResidenceFactory)
    flat = factory.SubFactory(FlatFactory)

    class Meta:
        model = models.ResidenceFlat


class StudentFactory(factory.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    number = factory.LazyAttribute(lambda o: 'abcde01%s' % o.user.name.strip(''))

    class Meta:
        model = models.Student


class ApplicationFactory(factory.DjangoModelFactory):
    flat = factory.SubFactory(FlatFactory)
    applicant = factory.SubFactory(UserFactory)
    status = random.choices["NEW", "REVIEW"]
    residence = factory.SubFactory(ResidenceFactory)

    class Meta:
        model = models.Application
