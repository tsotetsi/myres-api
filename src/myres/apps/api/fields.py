from django.utils import six
from rest_framework import serializers


class EnumField(serializers.ChoiceField):

    def __init__(self, enum, **kwargs):
        self.enum = enum
        kwargs['choices'] = [(e.value, e.name) for e in enum]
        super(EnumField, self).__init__(**kwargs)

    def to_representation(self, value):
        return self.choice_strings_to_values.get(six.text_type(value), value)

    def to_internal_value(self, data):
        try:
            return self.choice_strings_to_values[six.text_type(data)]
        except KeyError:
            self.fail('invalid_choice', input=data)
