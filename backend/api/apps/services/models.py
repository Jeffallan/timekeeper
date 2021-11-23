from django.db import models
from api.apps.core.models import TimestampedModel
from api.apps.users.models import Profile
from api.apps.core.util.services import ServiceChoices


class Service(TimestampedModel):
    name = models.CharField(max_length=140, unique=True)
    service_type = models.CharField(max_length=25, choices=[(x.value, x.name) for x in ServiceChoices])
    is_duration = models.BooleanField(default=False)
    approved_provider = models.ManyToManyField(Profile)