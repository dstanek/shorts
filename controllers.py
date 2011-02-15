"""A really simple url shortener for App Engine."""

from google.appengine.api import users
from snakeguice import inject
from snakeguice.config import Config
from mako.template import Template
import webob

import interfaces


class ShortsController(object):

    @inject(auth_service=interfaces.AuthService,
            short_service=interfaces.LinkShorteningService)
    def __init__(self, auth_service, short_service):
        self.auth_service = auth_service
        self.short_service = short_service

    def index(self, request):
        t = Template(filename='index.mako')
        return webob.Response(t.render(links=self.short_service.last(5),
                                       base_url=request.host_url))

    def create(self, request):
        if not self.auth_service.authorize(users.get_current_user()):
            # this could be handled better, but I'm lazy
            location = users.create_login_url(request.application_url)
            return webob.exc.HTTPFound(location=location)

        # I'm purposely not validating yet. I'm not a moron.
        link = self.short_service.create_link(request.POST.get('url'))

        location = '/#created:{0}'.format(
                link.shortened_url(request.host_url))
        return webob.exc.HTTPMovedPermanently(location=location)

    def redirect(self, request, code):
        link = self.short_service.get_link(code=code)
        if not link:
            return webob.exc.HTTPNotFound()
        return webob.exc.HTTPMovedPermanently(location=link.url)

    def favicon(self, request):
        return webob.exc.HTTPNotFound() # maybe i can implement this later...
