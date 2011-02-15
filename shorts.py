"""A really simple url shortener for App Engine."""

import os

from google.appengine.ext.webapp.util import run_wsgi_app
from snakeguice import create_injector, config, modules
from snakeguice.extras import snakeweb

import interfaces
import controllers
import models
import auth


DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Dev')


class ShortsModule(modules.Module):

    def configure(self, binder):
        binder.bind(interfaces.AuthService, to=auth.MeAuthService)
        binder.bind(interfaces.LinkShorteningService,
                    to=models.LinkShorteningService)

        if DEBUG:
            config_loader = config.ConfigParserLoader('app_dev.cfg')
        else:
            config_loader = config.ConfigParserLoader('app_prod.cfg')
        config_loader.short_name = ''
        config_loader.bind_configuration(binder)


class RoutesModule(snakeweb.RoutesModule):

    def configure(self, routes_binder):
        bind = lambda s, c, a:\
                routes_binder.connect(s, controller=c, action=a)
        bind('/', controllers.ShortsController, 'index')
        bind('/create', controllers.ShortsController, 'create')
        bind('/favicon.ico', controllers.ShortsController, 'favicon')
        bind('/:code', controllers.ShortsController, 'redirect')


def main():
    injector = create_injector([ShortsModule(), RoutesModule()])
    application = snakeweb.Application(injector)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
