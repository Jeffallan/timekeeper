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


