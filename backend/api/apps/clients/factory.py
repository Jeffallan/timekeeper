import factory
from api.apps.users.factory import Contact, active_choice
from api.apps.users.models import User
from datetime import datetime
import random

import api.apps.clients.models as models


class ClientContact(Contact):
    class Meta:
        model = models.Client

class LocationContact(Contact):
    class Meta: 
        model = models.Location

def users():
    u = User.objects.all().values_list("id", flat=True)
    print(u)
    return u

class Client(ClientContact):
    is_active = factory.LazyFunction(active_choice)
    name = factory.Faker("company")
    #location = factory.RelatedFactory("api.apps.clients.factory.Location", factory_related_name="client")

class Location(LocationContact):
    is_active = factory.LazyFunction(active_choice)
    client = factory.Iterator(models.Client.objects.all())#factory.SubFactory(Client, location=None)
    #providers = random.choice(User.objects.all().values_list('id', flat=True))
    name = factory.Faker("company")