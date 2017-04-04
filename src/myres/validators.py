from django.core.validators import RegexValidator


class E164Validator(RegexValidator):
    regex = r'^\+\d{11,15}$'
    message = "Number must comply to E164. Format '+27831234567' minimum 11 and maximum 15 digits."
