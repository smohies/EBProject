from django.test import TestCase
from unittest import mock
from ebproject import views

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

class MockRequest:
    def __init__(self, method, POST):
        self.method = method
        self.POST = POST

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

    def mock_request_post_200(*args, **kwargs):
        return MockResponse({}, status_code=200)

    def mock_request_post_422(*args, **kwargs):
        return MockResponse({}, status_code=422)

    def mock_request_post_400(*args, **kwargs):
        return MockResponse({}, status_code=400)

    @mock.patch('requests.get', side_effect=mock_requests_get_properties)
    def test_home_get(self, mock_get):
        result = views.home("")
        self.assertTrue(result)
        self.assertEqual(200, result.status_code)

    @mock.patch('requests.get', side_effect=mock_requests_get_401)
    def test_home_401(self, mock_get):
        with self.assertRaises(KeyError):
            views.home('')

    @mock.patch('requests.post', side_effect=mock_request_post_200)
    def test_leads_ok(self, mock_get):
        mock_body = {
            "name": "John",
            "phone": "123",
            "email": "mail@mail.com",
            "public_id": "EB-B5338",
            "message": "please halp!",
            "source": "mydomain.com"
        }
        request = MockRequest(method='POST', POST=mock_body)
        result = views.leads(request)
        self.assertEquals(200, result.status_code)

    @mock.patch('requests.post', side_effect=mock_request_post_422)
    def test_leads_error(self, mock_get):
        mock_body = {
            "name": "John",
            "phone": "123",
            "email": "mail@mail.com",
            "public_id": "EB-B5338",
            "message": "please halp!",
            "source": "mydomain.com"
        }
        request = MockRequest(method='POST', POST=mock_body)
        result = views.leads(request)
        self.assertEquals(422, result.status_code)

    def test_leads_invalid(self):
        mock_body = {}
        request = MockRequest(method='POST', POST=mock_body)
        result = views.leads(request)
        self.assertEquals(400, result.status_code)