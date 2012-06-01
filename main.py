from google.appengine.api import oauth
import logging
import traceback
import webapp2


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.post()

  def post(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hi there!\n')

    scope = 'https://www.googleapis.com/auth/userinfo.email'
    self.response.write('\noauth.get_current_user(%s)' % repr(scope))
    try:
      user = oauth.get_current_user(scope)
      self.response.write(' = %s\n' % user)
      self.response.write('- auth_domain = %s\n' % user.auth_domain())
      self.response.write('- email       = %s\n' % user.email())
      self.response.write('- nickname    = %s\n' % user.nickname())
      self.response.write('- user_id     = %s\n' % user.user_id())
    except oauth.OAuthRequestError, e:
      self.response.set_status(200)
      self.response.write(' -> %s %s\n' % (e.__class__.__name__, e.message))
      logging.warn(traceback.format_exc())


app = webapp2.WSGIApplication([
  ('/.*', MainHandler)
], debug=True)
