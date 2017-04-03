from collections import OrderedDict

from django.utils import six
from rest_framework import serializers


class ChoiceField(serializers.ChoiceField):

    def __init__(self, *args, **kwargs):
        choices = kwargs.get('choices')
        self._choices = OrderedDict(choices)
        super(ChoiceField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        return self.choice_strings_to_values.get(six.text_type(value), value)

    def to_internal_value(self, data):
        try:
            return self.choice_strings_to_values[six.text_type(data)]
        except KeyError:
            self.fail('invalid_choice', input=data)
