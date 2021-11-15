from .models import User, Profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from djoser.signals import user_activated
from api.apps.core.email import PasswordResetEmail

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def send_pwd_email():
#    pass

@receiver(user_activated)
def set_initail_password(sender, user, request, **kwargs):
    mail = PasswordResetEmail()
    #mail.usr = user
    #mail.get_context_data(usr=user)
    mail.usr = user
    mail.send(to=[user.email])