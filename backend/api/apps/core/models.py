from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created', '-updated']

class ContactInfoModel(TimestampedModel):
    address_1 = models.CharField(max_length=140, blank=True, null=True)
    address_2 = models.CharField(max_length=140, blank=True, null=True)
    city = models.CharField(max_length= 140, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.PositiveIntegerField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    # TODO  best way to validate this information

    class Meta:
        abstract = True

    @property
    def mailing_address(self):

        if self.address_1 and self.city and self.state and self.zip_code:
            return f"{self.address_1} {self.address_2} {self.city} {self.state} {self.zip_code}".replace("  ", " ")
        return ""
