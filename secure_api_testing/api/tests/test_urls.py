from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from api.views import CustomerView, CustomerDetailView
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


class TestApiUrls(SimpleTestCase):

    def test_get_customer_url_is_resolves(self):
        url = reverse("customer")
        self.assertEquals(resolve(url).func.view_class, CustomerView)
        print("customer url test passed !!!")

    def test_get_customer_detail_url_is_resolves(self):
        url = reverse("customer-detail", args=[1])
        self.assertEquals(resolve(url).func.view_class, CustomerDetailView)
        print("customer detail url test passed !!!")

#
# class TestCustomerAPIView(APITestCase):
#     customer_url = reverse('customer')
#     print('customer', customer_url)
#     user = User.objects.create_user(username='admin', password='some-strong-password')
#     print(user)
#
#     def setUp(self):
#         print("setup method")
#         self.user = User.objects.create_user(username='admin', password='some-strong-password')
#         print("user :", self.user)
#         self.token = Token.objects.create(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
#         print("user :", self.user)
#         print("token :", self.token)
#         print("client :", self.client)
