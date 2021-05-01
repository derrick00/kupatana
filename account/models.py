from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  #associate users with profiles
                                on_delete=models.CASCADE)  #all related profile gets deleted when user is deleted
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
            return f' Profile for user {self.user.username}'
# Create your models here.
