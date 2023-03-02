"""
Tests for the health check API.
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

HEALTH_CHECK_URL = reverse('health-check')


class HealthCheckApiTests(TestCase):
    """Tests the health check API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_health_check(self):
        res = self.client.get(HEALTH_CHECK_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
