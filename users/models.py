from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    dob = models.DateField(null=True, blank=True)
    




    def __str__(self):
        return "Профиль пользователя {}".format(self.user.username)

    class Meta:
        verbose_name_plural = 'Профили пользователей'
        verbose_name = 'Профиль пользователя'