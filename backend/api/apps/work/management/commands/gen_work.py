from django.core.management.base import BaseCommand
from django.db import models, transaction
from typing import Any, Optional
import random

from api.apps.clients.models import Location
from api.apps.services.models import Service
from api.apps.users.models import User
from api.apps.work.models import WorkPerformed
from api.apps.work.factory import WorkFactory


WORK = 200

def gen_loc() -> int:
    print("Creating location.")
    lst = Location.objects.all().values_list("id", flat=True)
    return random.choice(lst)

def gen_providers(id: int) -> int:
    print("Creating provider.")
    loc = Location.objects.get(pk=id)
    lst = loc.providers.values_list("id", flat=True)
    return random.choice(lst)

def gen_service(id: int) -> int:
    print("Creating service.")
    lst = Service.objects.filter(approved_providers=id).values_list("id", flat=True)
    return random.choice(lst)


class Command(BaseCommand):
    help = "Generates test data for services rendered."
    models = [WorkPerformed,]

    @transaction.atomic
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Creating test data.")
        self.stdout.write("Creating services rendered.")

        WorkPerformed.objects.all().delete()

        for _ in range(WORK):
            #loc = gen_loc()
            #print("location id", loc)
            #prov = gen_providers(loc)
            #print("provider id", prov)
            #svc = gen_service(prov)
            #print("service id", svc)
            #sv = WorkFactory.create(location=Location.objects.get(pk=loc).id,
            #                        provider=User.objects.get(pk=prov).id,
            #                        service=Service.objects.get(pk=svc).id,)
            sv = WorkFactory()