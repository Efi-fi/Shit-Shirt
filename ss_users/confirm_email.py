from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site

from shit_shirt import settings


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def send_confirm_email(user, request):
    subject = 'Shit|Shirt'
    from_email = settings.EMAIL_HOST_USER
    to_list = [user.email, settings.EMAIL_HOST_USER]
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    activation_link = f"{get_current_site(request)}/users/activate/uid={uid}/token={token}"

    message = f"Hello {user.username},\n {activation_link}"
    send_mail(subject, message, from_email, to_list, fail_silently=True)
