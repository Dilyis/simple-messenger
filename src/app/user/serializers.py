from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password',
                  'confirm_password')

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError(_('Passwords are not equal'))
        errors = {}
        try:
            # validate the password and catch the exception
            validate_password(password=password)
        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise ValidationError(errors)
        return attrs

    def create(self, validated_data):
        master = super(CreateUserSerializer, self).create(validated_data)
        master.set_password(validated_data['password'])
        master.save(update_fields=('password',))
        return master


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

