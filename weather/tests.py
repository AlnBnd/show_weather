from django.test import TestCase
from django.urls import reverse
from .models import City
from http import HTTPStatus

class IndexTestCase(TestCase):
    def setUp(self):
        pass

    def test_view_get(self):
        path = reverse('index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # self.assertIn('index.html', response.template_name)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_post_city(self):
        path = reverse('index')
        response = self.client.post(path, {'city_name': 'Moscow'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Weather in Moscow')
        self.assertTrue(City.objects.filter(city_name='Moscow').exists())

