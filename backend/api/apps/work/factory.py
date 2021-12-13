from factory.base import Factory
from api.apps.work.models import WorkPerformed
import factory
from factory.django import DjangoModelFactory
import random

from api.apps.users.models import User
from api.apps.services.models import Service
from api.apps.clients.models import Location



class WorkFactory(DjangoModelFactory):
    class Meta:
        model = WorkPerformed
    service_date = factory.Faker("date_this_decade")
    start_time = factory.Faker("time")
    stop_time = factory.Faker("time")
    billed = factory.Faker("boolean")
    location = factory.Iterator(Location.objects.all())
    provider = factory.Iterator(User.objects.all())
    service = factory.Iterator(Service.objects.all())
    units = random.uniform(1.00, 24.00)

"""
    @factory.post_generation
    def location(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for e in extracted:
                self.location.add(e)

    @factory.post_generation
    def provider(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for e in extracted:
                self.provider.add(e)

    @factory.post_generation
    def service(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for e in extracted:
                self.service.add(e)
"""