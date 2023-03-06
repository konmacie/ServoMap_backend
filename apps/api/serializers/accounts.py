from django.contrib.auth import (
    authenticate, get_user_model, update_session_auth_hash)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ImproperlyConfigured

from rest_framework import serializers

USER_MODEL = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    """
    Serializer used in LoginAPIView to validate user credentials.
    Doesn't log user in, just checks credentials and returns User instance
    for valid data. Call Django's login() manually to sign user in.
    ! Call .is_valid() before getting user, to run validators
    Use get_user() to get user instance. Note: before validation and for
    invalid credentials will return None.
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(read_only=True)

    _user = None

    class Meta:
        model = USER_MODEL
        fields = ('id', 'username', 'password', 'email')

    def validate(self, data):
        """
        Validate user credentials and set user instance for valid data.
        """
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user and not user.is_active:
                # Will never proc, since default authentication backend
                # returns None for inactive users.
                # Will work if AllowAllUsersModelBackend used.
                raise serializers.ValidationError('Account deactivated.')
            self._user = user
            # set instance, so user can be serialized by accessing .data
            self.instance = user
        if not self._user:
            raise serializers.ValidationError("Wrong username/password")
        return data

    def get_user(self):
        return self._user


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.
    Requred fields: username, email, password, password2.
    Validates if both passwords are identical and creates new user.
    """
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = USER_MODEL
        fields = ('id', 'username', 'password', 'password2', 'email')

    def validate_password(self, value):
        """
        Validate entered password using Django's built-in validators.
        """
        validate_password(value)
        return value

    def validate(self, data):
        """
        Check if both passwords are identical.
        """
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError(
                {'password2': 'Passwords do not match'})
        return data

    def create(self, validated_data):
        """
        Create user account using model manager's .create_user() method.
        """

        # Remove unnecessary password2 from data
        validated_data.pop('password2')

        # Get User model and create new user account.
        # Password hashed by .create_user method, no need to do it manually.
        model = self.Meta.model
        instance = model.objects.create_user(**validated_data)
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating authenticated users. If changing password,
    user must provide their actual one.
    Read-only fields: username.
    Required fields: email.
    Optional fields: password_old, password, password2*.
    * if any of the password fields was provided, validate if all of them
    were filled.
    """

    # allow for blank passwords in case if user isn't changing current one.
    password = serializers.CharField(
        required=True, write_only=True, allow_blank=True)
    password2 = serializers.CharField(
        required=True, write_only=True, allow_blank=True)
    password_old = serializers.CharField(
        required=True, write_only=True, allow_blank=True)

    class Meta:
        model = USER_MODEL
        fields = ('id', 'username', 'password_old',
                  'password', 'password2', 'email')
        # ? Should user be allowed to change username or email? TBD
        read_only_fields = ('username',)

    def validate(self, data):
        """
        If any of the password fields was provided, validate if all of them
        were filled.
        """
        password = data.get('password', "")
        password_confirm = data.get('password2', "")
        password_old = data.get('password_old', "")

        # If any of the password fields was filled, validate them.
        # No need for password validation if password isn't changed.
        if any([password, password_confirm, password_old]):
            # check if all passwords provided
            if not all([password, password_confirm, password_old]):
                raise serializers.ValidationError(
                    "To change the password, please fill all of the fields."
                )

            # check if pwd and confirmation pwd are identical
            if password != password_confirm:
                raise serializers.ValidationError(
                    {'password2': 'Passwords do not match'})

            # check if valid current password provided
            if not authenticate(username=self.instance.username,
                                password=password_old):
                raise serializers.ValidationError(
                    {'password_old': "Invalid current password."})

            # validate new password using Django's built-in validators
            validate_password(password)

        return data

    def update(self, instance, validated_data):
        """
        Update user instance.
        If password is changed, update session hash so user stays logged in.
        """
        # remove unnecessary data
        validated_data.pop('password_old', None)
        validated_data.pop('password2', None)

        # set new password if provided
        _pass_changed = False
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
            _pass_changed = True

        # update rest of instance's fields and save
        instance = super().update(instance, validated_data)
        if _pass_changed and self.context['request']:
            print('changed')
            update_session_auth_hash(self.context['request'], instance)
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for retrieving users' public data (id and username).
    Not serializing email.
    """
    class Meta:
        model = USER_MODEL
        fields = ('id', 'username')
