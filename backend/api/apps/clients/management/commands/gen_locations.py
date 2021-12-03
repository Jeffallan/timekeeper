from django.core.management.base import BaseCommand
from django.db import models, transaction
from typing import Any, Optional
import random

from api.apps.clients.factory import Client, Location
import api.apps.clients.models as models
from api.apps.users.models import User


CLIENT = 5
LOCATION = 5

def gen_providers():
    lst = User.objects.filter(is_active=True).values_list("id", flat=True)
    return random.choices(lst, k=random.randint(3,7))

class Command(BaseCommand):
    help = "Generates test data for clients and locations."
    models = [Client, Location]

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Creating test data.")
        self.stdout.write("Creating clients.")

        models.Location.objects.all().delete()
        #for _ in range(CLIENT):
        #    client = Client()

        self.stdout.write("Creating locations.")
        for _ in range(LOCATION):
            loc = Location.create(providers=gen_providers())