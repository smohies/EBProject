from django.conf import settings
from requests.auth import AuthBase

class TokenAuth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers[settings.EB_AUTH_HEADER_KEY] = f'{self.token}'
        return r