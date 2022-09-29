from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.test import SimpleTestCase


class TestCustomerAPIView(APITestCase):
    customers_url = reverse('customer')

    # print("customer :", customers_url)

    def setUp(self):
        print("setup method")
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # print("user :", self.user)
        # print("token :", self.token)
        # print("client :", self.client)

    def tearDown(self):
        pass

    def test_get_customers_authenticated(self):
        response = self.client.get(self.customers_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("test_get_customers_authenticated passed")

    def test_get_customer_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.customers_url)
        self.assertEquals(response.status_code, 401)
        print("test_get_customer_un_authenticated passed")

    def test_post_customer_authenticated(self):
        data = {
            "title": "Mr",
            "name": "Peter",
            "last_name": "Parker",
            "gender": "M",
            "status": "published",
        }
        # print(data)
        response = self.client.post(self.customers_url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(response.data['name'], "Peter")

        print("test_post_customer_authenticated passed")


class TestCustomerDetailApiViews(APITestCase):
    customers_url = reverse("customer")
    customer_url = reverse("customer-detail", args=[1])

    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Saving User
        data = {
            "title": "Mr",
            "name": "Vaibhav",
            "last_name": "Makde",
            "gender": "M",
            "status": "published",
        }
        print(data)

        response = self.client.post(self.customers_url, data, format='json')

    def test_get_customer_authenticated(self):
        response = self.client.get(self.customer_url)
        self.assertEquals(response.status_code, 200)
        print('test_get_customer_authenticated passed')

    def rest_get_customer_un_authentcated(self):
        self.client.force_authenticated(user=None, token=None)
        response = self.client.get(self.customer_url)
        self.assertEquals(response.status_code, 401)
        print('rest_get_customer_un_authentcated passed')

    def test_delete_customer_un_authentcated(self):
        print("delete test")
        response = self.client.delete(self.customer_url)
        print(response.status_code)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        print("Delete method passed")

