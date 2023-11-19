from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


class CustomEmailValidator(EmailValidator):
    def __call__(self, value):
        super().__call__(value)

        if value.endswith('@example.com'):
            raise ValidationError(
                _("Email addresses from example.com domain are not allowed.")
            )
