from django.test import TestCase
from django.http import response
from django.urls import reverse
import pytest


class SnacksTest(TestCase):

    def test_home_page_status(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)