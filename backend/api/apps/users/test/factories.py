import factory


class BasicUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'


    id = factory.Faker('random_number')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    role = 3
    password = "passpass123"

class SuperUserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = 'users.User'


    id = factory.Faker('random_number')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = True
    is_superuser = True
    role = 1
    password = "passpass123"
