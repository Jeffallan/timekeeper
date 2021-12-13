from django.core.management.base import BaseCommand
from django.db import models, transaction
from typing import Any, Optional

from api.apps.clients.factory import Client, Location
import api.apps.clients.models as models


CLIENT = 5
LOCATION = 5

class Command(BaseCommand):
    help = "Generates test data for clients and locations."
    models = [Client, Location]

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Creating test data.")
        self.stdout.write("Creating clients.")

        models.Client.objects.all().delete()

        for _ in range(CLIENT):
            client = Client()

        #self.stdout.write("Creating locations.")
        #for _ in range(LOCATION):
        #    loc = Location()