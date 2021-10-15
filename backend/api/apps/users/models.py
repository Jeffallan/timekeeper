from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
#from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from api.apps.core.util.users import UserChoice


# https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318
# https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username

class UserManager(BaseUserManager):

  # TODO raise value errors for first name and last name?
  def _create_user(self, email, password, role, is_staff, is_superuser, active, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        role=role,
        is_staff=is_staff,
        is_active=active,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, role,**extra_fields):

    return self._create_user(email, password, role, False, False, False, **extra_fields)

  def create_superuser(self, email, password, role=UserChoice.Maintenance.value, **extra_fields):
    user=self._create_user(email, password, role, True, True, True, **extra_fields)
    user.save(using=self._db)
    return user





class User(AbstractBaseUser, PermissionsMixin):


    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    has_joined = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=[(x.value, x.name) for x in UserChoice]
                                          , default=UserChoice.Audience.value)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name' ]
   

    objects = UserManager()

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})
