from rest_framework import serializers
from .models import User, Profile
from django.utils.crypto import get_random_string
from dry_rest_permissions.generics import DRYPermissionsField
from rest_flex_fields import FlexFieldsModelSerializer


class CreateUserSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(CreateUserSerializer, self).__init__(*args, **kwargs)
        self.fields['password'].required = False

    def create(self, validated_data):
        if "password" in validated_data.keys():
            password = validated_data["password"]
        else:
            password = get_random_string()

        user = User.objects.create_user(
                                          email = validated_data['email'],
                                          password = password,
                                          role = validated_data["role"],
                                       )
        user.set_password(password)
        user.save() # required to issue a valid auth token for user activation and password resets
        return user

    class Meta:
        model = User
        fields = ('id', 'password',  'email',  'role') # 'role' 'auth_token',
        #read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    # initial user password
    # https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
    # https://django-authtools.readthedocs.io/en/latest/how-to/invitation-email.html
    # https://djoser.readthedocs.io/en/latest/settings.html#serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "role", "is_active"]
        read_only_fields = ["role", "is_active", "email"]

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "role", "is_active", "role"]
        read_only_fields = ["email",]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    permissions = DRYPermissionsField()
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "address_1", "address_2", "city", "state", "zip_code", "phone_number", "mailing_address", "user", "permissions"]

class AdminProfileSerializer(serializers.ModelSerializer):
    user = AdminUserSerializer(read_only=True)
    permissions = DRYPermissionsField()
    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "address_1", "address_2", "city", "state", "zip_code", "phone_number", "mailing_address", "user", "permissions"]


class IncludeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        fields = ["id", "first_name", "last_name", "address_1", "address_2", "city", "state", "zip_code", "phone_number", "mailing_address", "user",]
        model = Profile