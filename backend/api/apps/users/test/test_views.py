from django.urls import reverse
from django.contrib.auth.hashers import check_password
from nose.tools import ok_, eq_
from rest_framework.test import APITestCase
from rest_framework import status
from faker import Faker
import factory
from api.apps.users.models import User
from .factories import BasicUserFactory
from django.test import Client
from api.config import common as settings

fake = Faker()

class TestBasicUserListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = factory.build(dict, FACTORY_CLASS=BasicUserFactory)
        self.user=BasicUserFactory()
        self.client.force_login(user=self.user)

    def test_post_request_with_no_data_unauthorized(self):
        response = self.client.post(self.url, {})
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_request_with_valid_data_unauthorized(self):
        response = self.client.post(self.url, self.user_data)
        eq_(response.status_code, status.HTTP_403_FORBIDDEN)


class TestBasicUserDetailTestCase(APITestCase):
    """
    Tests /users detail operations.
    """

    def setUp(self):
        self.user = BasicUserFactory()
        self.user_data = factory.build(dict, FACTORY_CLASS=BasicUserFactory)
        self.url = "/api/v1/auth/users/me/"
        self.direct_url = f"/api/v1/auth/users/"
        self.client.force_login(user=self.user)

    def test_get_me_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        eq_(response.status_code, status.HTTP_200_OK)

    def test_put_me_request_updates_a_user(self):
        payload = {**self.user_data}
        response = self.client.put(self.url, payload)
        eq_(response.status_code, status.HTTP_200_OK)

        user = User.objects.get(pk=self.user.id)
        #data = {k:v for k,v in vars(user).items() if k in ["id",
        #                                                   "email",
        #                                                   "first_name",
        #                                                   "last_name",
        #                                                   "is_active",
        #                                                   "is_staff",
        #                                                   "role",
        #                                                   "password"]}
        eq_(user.email, self.user_data["email"])

    def test_get_request_other_user_forbidden(self):
        other_user = BasicUserFactory()
        response = self.client.get(f"{self.direct_url}{other_user.id}/")
        eq_(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_cannot_change_roles_is_staff(self):
        self.client.patch(self.url, {"is_staff": True})
        user = User.objects.get(pk=self.user.id)
        eq_(vars(user)["is_staff"], False)

    def test_user_cannot_change_roles_is_superuser(self):
        self.client.patch(self.url, {"is_superuser": True})
        user = User.objects.get(pk=self.user.id)
        eq_(vars(user)["is_superuser"], False)

    def test_user_cannot_change_roles_custom_user_roles(self):
        response = self.client.patch(self.url, {"role": 1})
        user = User.objects.get(pk=self.user.id)
        eq_(vars(user)["role"], 3)
