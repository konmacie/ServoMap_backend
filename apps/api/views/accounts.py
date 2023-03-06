from django.contrib.auth import login as django_login, logout as django_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    GenericAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.serializers import accounts as accounts_serializers


@api_view(['GET', 'POST'])
def logout(request):
    django_logout(request)
    return Response({"detail": "Successfully logged out.", }, status=200)


@method_decorator(sensitive_post_parameters(), "dispatch")
@method_decorator(never_cache, "dispatch")
class LoginAPIView(GenericAPIView):
    """
    Authenticate user with provided credentials,
    start Django session.
    """
    serializer_class = accounts_serializers.LoginSerializer
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        _user = serializer.get_user()

        if _user:
            django_login(self.request, _user)
            # content = {
            #     'username': _user.username,
            #     'id': _user.pk
            # }
            return Response(serializer.data)
        return Response(
            {"detail": "Invalid username/password"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class WhoAmIAPIView(RetrieveAPIView):
    """
    Retrieve information about current user.
    """
    permission_classes = [IsAuthenticated]

    # using update serializer to retrieve all data, including email
    serializer_class = accounts_serializers.UserUpdateSerializer

    def get_object(self):
        return self.request.user


@method_decorator(sensitive_post_parameters(), "dispatch")
@method_decorator(never_cache, "dispatch")
class CreateUserAPIView(CreateAPIView):
    serializer_class = accounts_serializers.UserCreateSerializer
    http_method_names = ['post']


@method_decorator(sensitive_post_parameters(), "dispatch")
@method_decorator(never_cache, "dispatch")
class UpdateUserAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = accounts_serializers.UserUpdateSerializer
    http_method_names = ['post']

    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
