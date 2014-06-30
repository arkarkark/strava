#!/usr/bin/python

import subprocess
import stravalib
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import urlparse

client_id, secret = open('client.secret').read().strip().split(',')
port = 1969

url = 'http://localhost:%d/authorized' % port

client = stravalib.client.Client()
authorize_url = client.authorization_url(client_id=client_id, redirect_uri=url)
print 'Opening: %s' % authorize_url
subprocess.call(['open', authorize_url])

allDone = False

def UseCode(code):
  access_token = client.exchange_code_for_token(client_id=client_id,
                                                client_secret=secret, code=code)
  # Now store that access token somewhere (a database?)
  client.access_token = access_token
  athlete = client.get_athlete()
  print("For %(id)s, I now have an access token %(token)s" %
        {'id': athlete.id, 'token': access_token})

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_HEAD(self):
    return self.do_GET()

  def do_GET(self):
    self.wfile.write('<script>window.close();</script>')
    code = urlparse.parse_qs(urlparse.urlparse(self.path).query)['code'][0]
    global allDone
    allDone = True
    UseCode(code)

httpd = BaseHTTPServer.HTTPServer(('localhost', port), MyHandler)
while not allDone:
  httpd.handle_request()
