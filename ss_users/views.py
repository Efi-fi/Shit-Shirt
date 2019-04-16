from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_text

from . import logics, models, confirm_email


def email_required(func):
    def wrapper(request, user_id=None):
        if not models.MyUser.objects.get(username=request.user.username).confirm_email:
            return email(request)
        else:
            return func(request, user_id)

    return wrapper


@login_required(login_url='users/login')
@email_required
def user_page(request, user_id=None):
    if not user_id:
        user_id = request.user.id
    user = models.MyUser.objects.get(id=user_id)
    print(user.confirm_email)

    return render(request, 'user_page.html', {'user': user})


def login(request):
    message = 'Good day, we are glad to see you.'
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            message = 'The username or password were incorrect.'
        else:
            if not user.is_active:
                message = 'The account has been disabled, confirm your email.'
            else:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'login.html', {'message': message})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registration(request):
    message = logics.full_check(request)
    if not message:
        new_user = models.MyUser(username=request.POST['username'], email=request.POST['email'])
        new_user.set_password(request.POST['password1'])
        new_user.save()
        user = auth.authenticate(username=new_user.username, password=request.POST['password1'])
        auth.login(request, user)
        return email(request)

    return render(request, 'registration.html', {'message': message})


def email(request):
    user = models.MyUser.objects.get(username=request.user.username)

    if request.method == 'POST' and logics.check_email(request.POST['email']):
        print(request.POST)
        user.email = request.POST['email']
        confirm_email.send_confirm_email(user, request)
        user.confirm_email = False
        user.save()

    return render(request, 'email.html', {'user': user})


def activate_user_email(request, uid, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid))
        user = models.MyUser.objects.get(pk=uid)
    except:
        user = None
    if user and confirm_email.account_activation_token.check_token(user, token):
        user.confirm_email = True
        user.save()
        return email(request)
    else:
        logout(request)
        return HttpResponseRedirect('/')
