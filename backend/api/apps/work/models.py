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

    def __str__(self):
        return f"{self.location} {self.service} {self.service_date}"

    @staticmethod
    def has_read_permission(request):
        #print(vars(request))
        #return request.user == request.provider or request.user.role == 1
        return True

    def has_object_read_permission(self, request):
        return request.user == self.provider or request.user.role == 1

    @staticmethod   #also grants create permission
    def has_write_permission(request):
        #return request.user == request.object.provider or request.user.role == 1
        return True

    def has_object_write_permission(self, request): #includes delete
        if self.billed:
            return False
        return request.user == self.provider or request.user.role == 1

    def has_object_update_permission(self, request):
        if self.billed:
            return False
        return request.user == self.provider or request.user.role == 1
