from django.utils import timezone
from rest_framework import serializers

from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('receiver', 'message', 'subject')

    def save(self, **kwargs):
        kwargs['sender'] = self.context['request'].user
        kwargs['creation_date'] = timezone.now()
        return super(CreateMessageSerializer, self).save(**kwargs)