"""A really simple url shortener for App Engine."""

from google.appengine.ext import db

import base_n


class LinkShorteningService(object):

    def create_link(self, url):
        link = Link(url=url)
        link.put()
        return link

    def get_link(self, code):
        return Link.get_by_id(base_n.base62_decode(code))

    def last(self, num):
        q = Link.all()
        q.order('-created')
        return q.fetch(num)


class Link(db.Model):
    url = db.LinkProperty()
    created = db.DateTimeProperty(auto_now_add=True)

    def shortened_url(self, base_url=''):
        return base_url + '/' + base_n.base62_encode(self.key().id())
