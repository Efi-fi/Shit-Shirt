from django.db import models
from django.contrib.auth.models import User


class SSUser(User):
    confirm_email = models.BooleanField(default=False)
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    achivements = models.CharField(max_length=64, default='')
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = 's/s user'
        verbose_name_plural = 's/s users'
