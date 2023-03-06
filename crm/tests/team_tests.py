from unittest import mock

from django.core.exceptions import BadRequest
from django.test import TestCase, TransactionTestCase
from crm.models.team import Team
from crm.services.team import TeamService


class TeamListTestCase(TransactionTestCase):
    reset_sequences = True
    def setUp(self):
        Team.objects.create(code="ABCD", name="A B C", domain="domain", department="department")

    def tearDown(self):
        Team.objects.all().delete()

    def test_team_list_all(self):
        service = TeamService()
        teams = service.getAll()
        self.assertListEqual(teams,
             [
                 {
                     "id": 1,
                     "code": "ABCD",
                     "name": "A B C",
                     "domain": "domain",
                     "department": "department",
                     'sales': [],
                     "created": mock.ANY
                 }
            ]
        )

    def test_team_get_empty(self):
        service = TeamService()
        team = service.getByCode('AC')
        self.assertEqual(team, None)

    def test_team_get(self):
        service = TeamService()
        team = service.getByCode('ABCD')
        self.assertDictEqual(
            team,
             {
                 "id": 1,
                 "code": "ABCD",
                 "name": "A B C",
                 "domain": "domain",
                 "department": "department",
                 'sales': [],
                 "created": mock.ANY
             }
        )

    def test_customer_update(self):
        service = TeamService()
        team = service.update("ABCD", {"name": "updated name", 'domain': "domain 2"})
        self.assertDictEqual(
            team,
            {
             "id": 1,
             "code": "ABCD",
             "name": "updated name",
             "domain": "domain 2",
             "department": "department",
             'sales': [],
             "created": mock.ANY
            }
        )

    def test_customer_update_with_code(self):
        service = TeamService()
        with self.assertRaises(BadRequest):
            service.update("ABCD", {"name": "updated name", "code": "updated", "domain": "domain 2"})
