from django.db import models
from api.apps.core.models import ContactInfoModel
from api.apps.users.models import User


class Client(ContactInfoModel):
    name = models.CharField(max_length=140, unique=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


class Location(ContactInfoModel):

    name = models.CharField(max_length=140, unique=True)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    providers = models.ManyToManyField(User)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
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


