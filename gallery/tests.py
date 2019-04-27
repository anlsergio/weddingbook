import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):

    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        client = Client()
        response = client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        client = Client()
        response = client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_gallery_form_not_allowed(self):
        client = Client()
        response = client.get('/gallery/new/')
        self.assertEqual(response.status_code, 302)

    def test_image_approval_not_allowed(self):
        client = Client()
        response = client.get('/gallery/1/update/')
        self.assertEqual(response.status_code, 302)

    def test_image_deletion_not_allowed(self):
        client = Client()
        response = client.get('/gallery/1/delete/')
        self.assertEqual(response.status_code, 302)

    def test_image_deletion_not_allowed(self):
        client = Client()
        response = client.get('/gallery/1/delete/')
        self.assertEqual(response.status_code, 302)

    def test_image_waiting_approval_not_allowed(self):
        client = Client()
        response = client.get('/gallery/waiting_approval/')
        self.assertEqual(response.status_code, 302)

