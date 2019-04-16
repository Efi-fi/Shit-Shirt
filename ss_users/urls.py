from django.urls import re_path, path

from . import views

app_name = 'ss_users'

urlpatterns = [
    path('id<str:user_id>/', views.user_page, name='user_page'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('email/', views.email, name='email'),
    path('activate/uid=<str:uid>/token=<str:token>/', views.activate_user_email, name='activate'),
]
