from django.db import models
from api.apps.core.models import TimestampedModel
from api.apps.users.models import User
from api.apps.services.models import Service
from api.apps.clients.models import Location


class WorkPerformed(TimestampedModel):
    location = models.ForeignKey(to=Location, on_delete=models.DO_NOTHING, blank=False, null=False)
    provider = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, blank=False, null=False)
    service = models.ForeignKey(to=Service, on_delete=models.DO_NOTHING, blank=False, null=False)
    service_date = models.DateField()
    start_time = models.TimeField()
    stop_time = models.TimeField()
    billed = models.BooleanField(default=False)
    units = models.FloatField(default=1)

    # TODO add DRF Permissions
