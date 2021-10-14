from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from decimal import Decimal

def validate_duration(value):
    if value <= Decimal(0.25):
        raise ValidationError(
            _('%(value)s Minimum billabe time is 15 min.'),
            params={'value': value},
        )
    if value >= Decimal(24.0):
        raise ValidationError(
            _('%(value)s Submission exceeds maximum.'),
            params={'value': value},
    )