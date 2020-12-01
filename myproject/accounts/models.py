from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
# from django.db.models.signals import post_save
# from django.dispatch import receiver


class Profile(AbstractUser):
    dob = models.DateField(null=True, verbose_name=_('Date of birth:'))
    photo = models.ImageField(upload_to='profile_pics', default='profile_pics/user.jpg')

    def __str__(self):
        return self.username
