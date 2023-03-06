from unittest import mock

from django.test import TestCase, TransactionTestCase

from crm.models.customer import Customer
from crm.services.customer import CustomerService


class CustomerListTestCase(TransactionTestCase):
    reset_sequences = True
    def setUp(self):
        Customer.objects.create(name="name1", username="username", email='abcd@abcd.com')
        Customer.objects.create(name="name2", username="username2", email='abcd2@abcd.com')

    def tearDown(self):
        Customer.objects.all().delete()

    def test_customer_list_all(self):
        service = CustomerService()
        customers = service.getAll()
        self.assertListEqual(customers,
             [
                 {
                     "id": 2,
                     "salePerson": None,
                     "name": "name2",
                     "username": "username2",
                     "email": "abcd2@abcd.com",
                     "created": mock.ANY
                 },
                 {
                     "id": 1,
                     "salePerson": None,
                     "name": "name1",
                     "username": "username",
                     "email": "abcd@abcd.com",
                     "created": mock.ANY
                 }
            ]
        )

    def test_customer_create(self):
        service = CustomerService()
        customer = service.create({"name": "abcd", 'username': "name", "email": "qwerty@sdd.com"})
        self.assertDictEqual(customer,
             {
                 "id": 3,
                 "salePerson": None,
                 "name": "abcd",
                 "username": "name",
                 "email": "qwerty@sdd.com",
                 "created": mock.ANY
             }
        )

    def test_customer_update(self):
        service = CustomerService()
        customer = service.update(1, {"name": "updated name", 'username': "updated user name"})
        self.assertDictEqual(customer,
             {
                 "id": 1,
                 "salePerson": None,
                 "name": "updated name",
                 "username": "updated user name",
                 "email": "abcd@abcd.com",
                 "created": mock.ANY
             }
        )