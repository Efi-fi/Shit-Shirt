from django.db import models
from ss_users.models import SSUser


class Shirt(models.Model):
    title = models.CharField(max_length=32)
    # file
    gender = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    base_colors = (
        ('wt', 'white'),
        ('bk', 'black'),
        ('rd', 'red'),
        ('gn', 'green'),
        ('bl', 'blue')
    )
    themes = (
        ('none', 'none'),
        ('love', 'love'),
        ('humor', 'humor'),
        ('trip', 'trip'),
        ('fear', 'fear'),
        ('night', 'night'),
        ('sadness', 'sadness'),
        ('disco', 'disco'),
        ('fog', 'fog')
    )
    base_color = models.CharField(max_length=2, choices=base_colors, default='wt')
    sex = models.CharField(max_length=1, choices=gender, default='M')
    theme = models.CharField(max_length=8, choices=themes, default='none')
    description = models.TextField(max_length=256)
    tegs = models.TextField(max_length=256, blank=True, null=True)
    creator = models.ForeignKey(SSUser, on_delete=models.DO_NOTHING, null=True)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    created = models.DateTimeField(auto_now_add=True)
    value = models.rating = models.DecimalField(decimal_places=2, max_digits=8, default=0)


class Comment(models.Model):
    text = models.TextField(max_length=1024, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(SSUser, on_delete=models.DO_NOTHING, null=True)
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE, null=True)
