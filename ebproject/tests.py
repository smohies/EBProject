from django.test import TestCase
from unittest import mock
from ebproject import views

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class ViewsTestCase(TestCase):
    def mock_requests_get_properties(*args, **kwargs):
        return MockResponse(
            {
                "pagination": {"limit": 15, "page":1,
                "total": 481},
                "content": [{"public_id": "test"}]
            }, 200)
    
    def mock_requests_get_401(*args, **kwargs):
        return MockResponse({"error":"error"}, 401)

    @mock.patch('requests.get', side_effect=mock_requests_get_properties)
    def test_home_get(self, mock_get):
        result = views.home("")
        self.assertTrue(result)
        self.assertEqual(200, result.status_code)

    @mock.patch('requests.get', side_effect=mock_requests_get_401)
    def test_home_401(self, mock_get):
        with self.assertRaises(KeyError):
            views.home('')
