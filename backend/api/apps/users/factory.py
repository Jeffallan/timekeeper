import factory
from factory.django import DjangoModelFactory
from datetime import datetime
import random

from .models import User, Profile
from django.db.models.signals import post_save

########
# Docs #
#######
"""
https://faker.readthedocs.io/en/latest/providers/faker.providers.address.html
https://factoryboy.readthedocs.io/en/stable/reference.html?highlight=faker#faker
"""


def active_choice() -> bool:
    return random.choice([True, False])

@factory.django.mute_signals(post_save)
class AdminUser(DjangoModelFactory):
    class Meta:
        model = User
    email = "admin@mail.com"
    is_staff = True
    is_superuser = True
    is_active = True
    has_joined = True
    last_login = datetime.now()
    date_joined = datetime.now()
    role = 1
    password="passpass123"
    profile = factory.RelatedFactory("api.apps.users.factory.AdminProfile",
                                     factory_related_name='user')

@factory.django.mute_signals(post_save)
class ActiveUser(DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker("email")
    is_staff = False
    is_superuser = False
    is_active = True
    has_joined = True
    last_login = datetime.now()
    date_joined = datetime.now()
    role = 2
    password="passpass123"
    profile = factory.RelatedFactory("api.apps.users.factory.ActiveProfile",
                                     factory_related_name='user')


@factory.django.mute_signals(post_save)
class InactiveUser(DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker("email")
    is_staff = False
    is_superuser = False
    is_active = False
    has_joined = factory.LazyFunction(active_choice)
    last_login = datetime.now()
    date_joined = datetime.now()
    role = 2
    password="passpass123"
    profile = factory.RelatedFactory("api.apps.users.factory.InactiveProfile",
                                     factory_related_name='user')

@factory.django.mute_signals(post_save)
class Contact(DjangoModelFactory):
    class Meta:
        model = Profile
    address_1 = factory.Faker("street_address")
    address_2 = factory.Faker("building_number")
    city = factory.Faker("city")
    state = "NE"
    zip_code = factory.Faker("postcode")
    phone_number = factory.Faker("phone_number")
    created = datetime.now()
    updated = datetime.now()

@factory.django.mute_signals(post_save)
class AdminProfile(Contact):
    class  Meta:
        model = Profile
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    user = factory.SubFactory(AdminUser, profile=None)

@factory.django.mute_signals(post_save)
class ActiveProfile(Contact):
    class  Meta:
        model = Profile
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    user = factory.SubFactory(ActiveUser, profile=None)

@factory.django.mute_signals(post_save)
class InactiveProfile(Contact):
    class  Meta:
        model = Profile
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    user = factory.SubFactory(InactiveUser, profile=None)

