"""A really simple url shortener for App Engine."""

from snakeguice import inject
from snakeguice.config import Config


class MeAuthService(object):

    @inject(email=Config(':main:my_email'))
    def __init__(self, email):
        self.email = email

    def authorize(self, user):
        return user and user.email() == self.email
