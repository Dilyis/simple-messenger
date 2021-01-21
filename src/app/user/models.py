from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q

from user.manager import EmailUserManager


class User(AbstractUser):
    """
    Base end-user
    """
    email = models.EmailField('Email', unique=True)
    first_name = models.CharField('First name', max_length=150)
    last_name = models.CharField('Last name', max_length=150)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmailUserManager()

    class Meta:
        db_table = 'users'

    @property
    def name(self):
        return '{} {} '.format(self.first_name, self.last_name)

    def __str__(self):
        return self.name


class AdministratorManager(EmailUserManager):
    """
    Менеджер для получения администраторов
    """
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)

        return qs.filter(
            Q(is_staff=True) | Q(is_superuser=True))


class Administrator(User):
    """
    Proxy-model to admins
    """
    objects = AdministratorManager()

    class Meta:
        proxy = True
