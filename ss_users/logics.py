from .models import SSUser


def full_check(request):
    message = 'For registration you need to fill in all the fields'
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password1']
        if password1 == password2:
            if check_username(request.POST['username']):
                if check_email(request.POST['email']):
                    return None
                else:
                    message = 'Email ' + request.POST['email'] + ' is already taken or incorrect.'
            else:
                message = 'Username ' + request.POST['username'] + ' is already taken.'
        else:
            message = 'Passwords do not match.'
    return message


def check_username(username):
    try:
        SSUser.objects.get(username=username)
    except:
        return True


def check_email(email):
    if email:
        try:
            return True
            SSUser.objects.get(email=email)
        except:
            return True
