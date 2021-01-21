from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode as uid_encoder


def make_reset_password_link(user):
    """
    Make link to reset password
    """
    token = default_token_generator.make_token(user)
    uid = force_text(uid_encoder(force_bytes(user.id)))
    reset_link = urljoin(
        settings.FRONT_URL,
        settings.FRONT_PASSWORD_RESET.format(user_id=uid, token=token))
    return reset_link
