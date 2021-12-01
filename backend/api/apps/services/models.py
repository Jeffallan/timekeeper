from django.db import models
from api.apps.core.models import TimestampedModel
from api.apps.users.models import User
from api.apps.core.util.services import ServiceChoices


class Service(TimestampedModel):
    name = models.CharField(max_length=140, unique=True)
    service_unit = models.CharField(max_length=25, choices=[(x.value, x.name) for x in ServiceChoices])
    is_duration = models.BooleanField(default=False)
    approved_providers = models.ManyToManyField(User)

    def __str__(self):
        return self.name