from django.urls import re_path, path

from . import views

app_name = 'ss_main'

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    path('shirt/id<shirt_id>', views.shirt, name='shirt'),
    path('shirt/edit/id<shirt_id>', views.edit_shirt, name='edit_shirt')
]
