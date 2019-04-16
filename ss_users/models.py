from django.db import models
from django.contrib.auth.models import User


class MyUser(User):
    confirm_email = models.BooleanField(default=False)
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    # comments
    # achivements
    # shirts
    likes = models.IntegerField(default=0)
