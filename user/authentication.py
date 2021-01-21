from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailAuthBackend(ModelBackend):
    """Authorization by email
    """
    User = get_user_model()

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = self.User.objects.get(email=email)
        except self.User.DoesNotExist:
            return

        if user.check_password(password):
            return user
