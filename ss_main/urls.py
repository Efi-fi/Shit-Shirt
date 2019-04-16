from django.urls import re_path

from . import views

app_name = 'ss_main'

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
]