from __future__ import with_statement
import os
import logging
import cgi
import datetime
import urllib
import wsgiref.handlers
import random
import re

from google.appengine.dist import use_library
use_library('django', '1.2')
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class QuixeyJS(webapp.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/javascript'
        if self.request.get('timestamp'):
            self.response.headers['expires'] = format_http_date(
                datetime.datetime.utcnow() + datetime.timedelta(days=365)
            )
            self.response.headers['cache-control'] = 'public'
        self.response.out.write(js.get_js())

class ConstantsJS(webapp.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/javascript'
        self.response.headers['expires'] = format_http_date(
            datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        )
        self.response.headers['cache-control'] = 'public'
        self.response.out.write(js.get_constants())

class AdminJS(webapp.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/javascript'
        self.response.out.write(js.get_admin_js())

class JSFile(webapp.RequestHandler):
    def get(self, path):
        self.response.headers['content-type'] = 'text/javascript'
        contents = js.get_js_file(path, transform=False)
        if self.request.get('timestamp'):
            self.response.headers['expires'] = format_http_date(
                datetime.datetime.utcnow() + datetime.timedelta(days=365)
            )
            self.response.headers['cache-control'] = 'public'
        self.response.out.write(contents)

application = webapp.WSGIApplication(
                                     [
                                         ('/addbiz', AddBusiness),
                                         ('/dashboard', Dashboard),
                                         ('/makechange', Change),
                                         ('/validatecode', ValidateCode),
                                         ('/notfound', PageNotFound),
                                         ('/reviewsdata', Reviews),
                                         ('/', PageNotFound),
                                         ('/m/([^/]+)?', MainPage),
                                         ('/t/([^/]+)?', MainPage)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
