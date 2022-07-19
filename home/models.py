from django.db import models

# Create your models here.
class UserDetails(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    phone = models.IntegerField()
    # second_phone_number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.first_name)