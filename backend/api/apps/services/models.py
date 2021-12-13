from django.db import models
from api.apps.core.models import TimestampedModel
from api.apps.users.models import User
from api.apps.core.util.services import ServiceChoices


class Service(TimestampedModel):
    name = models.CharField(max_length=140, unique=True)
    service_unit = models.CharField(max_length=25, choices=[(x.value, x.name) for x in ServiceChoices])
    is_duration = models.BooleanField(default=False)
    providers = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    @staticmethod
    def has_read_permission(request):
        return True

    def has_object_read_permission(self, request):
        if request.user in self.providers.all():
            return True
        return request.user.role == 1

    @staticmethod   #also grants create permission
    def has_write_permission(request):
        return request.user.role == 1

    def has_object_write_permission(self, request): #includes delete
       return request.user.role == 1

    def has_object_update_permission(self, request):
        return request.user.role == 1
