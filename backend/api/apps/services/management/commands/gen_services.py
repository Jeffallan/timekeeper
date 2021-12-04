from django.core.management.base import BaseCommand
from django.db import models, transaction
from typing import Any, Optional, List
import random


from api.apps.users.models import User
from api.apps.services.models import Service
from api.apps.services.factory import ServiceFactory

SERVICE = 5

def gen_providers() -> List:
    lst = User.objects.filter(is_active=True).values_list("id", flat=True)
    return random.choices(lst, k=random.randint(3,7))


class Command(BaseCommand):
    help = "Generates test data for services and providers."
    models = [Service,]

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Creating test data.")
        self.stdout.write("Creating services.")

        Service.objects.all().delete()

        for _ in range(SERVICE):
            sv = ServiceFactory.create(approved_providers=gen_providers())