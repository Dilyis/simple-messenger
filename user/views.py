import http

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins
from rest_framework.compat import authenticate
from rest_framework.decorators import parser_classes, action
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from swagger import helpers
from .models import User
from .permissions import UserPermissions
from .serializers import UserSerializer, LoginSerializer, CreateUserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = User.objects
    serializer_class = UserSerializer
    permission_classes = (UserPermissions,)

    @swagger_auto_schema(
        request_body=CreateUserSerializer,
        responses={"200": openapi.Response(
            description="Пользователь",
            schema=UserSerializer)})
    @parser_classes([MultiPartParser])
    def create(self, request, *args, **kwargs):
        s = CreateUserSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.save()
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return Response(data)

    @action(methods=['get'], detail=False, url_path='current', url_name='current')
    @swagger_auto_schema(
        responses={"200": openapi.Response(
            description="Текущий пользователь",
            schema=UserSerializer)
        })
    def current(self, request, *args, **kwargs):
        s = self.get_serializer(request.user)
        return Response(s.data, status=http.HTTPStatus.CREATED)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = ()

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={"200": openapi.Response(
            description="Параметры",
            schema=helpers.obj({
                "refresh": helpers.string(),
                "access": helpers.string(),
                "user_id": helpers.number(),
                "first_name": helpers.string(),
                "last_name": helpers.string()})),
            '400': 'Validation error',
            '401': 'Authentication failed'})
    def post(self, request, *args, **kwargs):
        """Authentication
        HTTP_AUTHORIZATION: Token <TOKEN>
        """
        s = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = authenticate(email=s.data['email'], password=s.data['password'])

        if not user:
            raise AuthenticationFailed()

        refresh = RefreshToken.for_user(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name
        }
        return Response(data)
