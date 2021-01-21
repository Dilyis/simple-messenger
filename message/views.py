from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response

from message.models import Message
from message.permissions import MessagePermissions
from message.serializers import MessageSerializer, CreateMessageSerializer


class MessageViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.DestroyModelMixin,  GenericViewSet):
    queryset = Message.objects
    serializer_class = MessageSerializer
    permission_classes = (MessagePermissions, )
    filter_fields = ['unread']

    def get_queryset(self):
        qs = super().get_queryset().filter(
            Q(sender=self.request.user) | Q(receiver=self.request.user))
        return qs

    @swagger_auto_schema(
        request_body=CreateMessageSerializer,
        responses={HTTP_200_OK: openapi.Response(
            description="Message",
            schema=MessageSerializer)})
    def create(self, request, *args, **kwargs):
        serializer = CreateMessageSerializer(
            data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            self.get_serializer(serializer.instance).data,
            status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user == instance.receiver:
            instance.read()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserMessagesViewSet(ListAPIView):
    queryset = Message.objects
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated,)
    filter_fields = ['unread']

    def get_queryset(self):
        user_pk = self.kwargs["pk"]
        qs = super().get_queryset().filter(
            Q(sender=self.request.user, receiver=user_pk) |
            Q(sender=user_pk, receiver=self.request.user))
        return qs
