from django.db import models
from ss_users.models import SSUser


class Shirt(models.Model):
    title = models.CharField(max_length=32)
    # file
    describcion = models.TextField(max_length=256, blank=True, null=True)
    tegs = models.TextField(max_length=256, blank=True, null=True)
    creator = models.ForeignKey(SSUser, on_delete=models.DO_NOTHING, default=None)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(SSUser, on_delete=models.DO_NOTHING, default=None)
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE, default=None)
    # likes