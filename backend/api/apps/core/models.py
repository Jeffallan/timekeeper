from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

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
    #phone_number = PhoneNumberField(blank=True)
    # TODO  best way to validate this information

    class Meta:
        abstract = True

    @property
    def mailing_address(self):
        s = "{} {} {} {} {}".format(
                                        self.address_1, 
                                        self.address_2,
                                        self.city, 
                                        self.state, 
                                        self.zip_code
                                      )
        return s.replace("None", "")

