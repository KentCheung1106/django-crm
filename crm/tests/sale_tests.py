from unittest import mock
from django.test import TestCase, TransactionTestCase

from crm.models.sale import Sale
from crm.models.team import Team
from crm.services.sale import SaleService


class TeamListTestCase(TransactionTestCase):
    reset_sequences = True
    def setUp(self):
        team = Team.objects.create(code="ABCD", name="A B C", domain="domain", department="department")
        team2 = Team.objects.create(code="1234", name="1234", domain="domain", department="department")
        Sale.objects.create(name="Peter", email="abcd@qnn.com", company="company", team=team)

    def tearDown(self):
        Sale.objects.all().delete()
        Team.objects.all().delete()

    def test_team_list_all(self):
        service = SaleService()
        sales = service.getAll()
        self.assertListEqual(sales,
             [
                 {
                     "id": 1,
                     "customers": [],
                     "team": {
                         "id": 1,
                         "code": "ABCD",
                         "name": "A B C",
                         "domain": "domain",
                         "department": "department",
                         "created": mock.ANY
                     },
                     "name": "Peter",
                     "email": "abcd@qnn.com",
                     "company": "company",
                     "created": mock.ANY
                 }
            ]
        )

    def test_sale_create(self):
        service = SaleService()
        sale = service.create({
            "name": "qwert",
            "email": "qwert@example.com",
            "company": "qwert",
            "team": 1
        })

        self.assertDictEqual(
            sale,
            {
                "id": 2,
                "customers": [],
                "team": {
                    "id": 1,
                    "code": "ABCD",
                    "name": "A B C",
                    "domain": "domain",
                    "department": "department",
                    "created": mock.ANY
                },
                "name": "qwert",
                "email": "qwert@example.com",
                "company": "qwert",
                "created": mock.ANY
            }
        )
    def test_sale_get(self):
        service = SaleService()
        sale = service.getById(1)

        self.assertDictEqual(
            sale,
            {
                "id": 1,
                "customers": [],
                "team": {
                    "id": 1,
                    "code": "ABCD",
                    "name": "A B C",
                    "domain": "domain",
                    "department": "department",
                    "created": mock.ANY
                },
                "name": "Peter",
                "email": "abcd@qnn.com",
                "company": "company",
                "created": mock.ANY
            }
        )

    def test_customer_update(self):
        service = SaleService()
        sale = service.update(1, {"name": "Mary", "email": "mary@hcdc.com", "team": 2})
        self.assertDictEqual(
            sale,
            {
                "id": 1,
                "customers": [],
                "team": {
                    "id": 2,
                    "code": "1234",
                    "name": "1234",
                    "domain": "domain",
                    "department": "department",
                    "created": mock.ANY
                },
                "name": "Mary",
                "email": "mary@hcdc.com",
                "company": "company",
                "created": mock.ANY
            }
        )
