from api.apps.services.models import Service
from api.apps.users.models import User
import factory
from factory.django import DjangoModelFactory
from datetime import datetime
import random

from api.apps.users.factory import active_choice
from api.apps.core.util.services import ServiceChoices


class ServiceFactory(DjangoModelFactory):
    class Meta:
        model = Service
    name = factory.Faker("job")
    service_unit = random.choice([x.name for x in ServiceChoices])
    is_duration =  factory.LazyFunction(active_choice)

    @factory.post_generation
    def approved_providers(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for provider in extracted:
                self.approved_providers.add(provider)