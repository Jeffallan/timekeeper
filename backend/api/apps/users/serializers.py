from rest_framework import serializers
from .models import User
from django.utils.crypto import get_random_string


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
                                          first_name = validated_data['first_name'], 
                                          last_name = validated_data['last_name'],
                                          email = validated_data['email'],
                                          password = password,
                                          role = validated_data["role"],
                                       )
        user.set_password(password)
        user.save() # required to issue a valid auth token for user activation and password resets 
        return user

    class Meta:
        model = User
        fields = ('id', 'password', 'first_name', 'last_name', 'email',  'role') # 'role' 'auth_token',
        #read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}

    # initial user password
    # https://stackoverflow.com/questions/16857450/how-to-register-users-in-django-rest-framework
    # https://django-authtools.readthedocs.io/en/latest/how-to/invitation-email.html
    # https://djoser.readthedocs.io/en/latest/settings.html#serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "full_name", "email", "role"]
        read_only_fields = ['role',]

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "full_name", "email", "role"]

