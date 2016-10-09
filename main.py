import json
import os

import jinja2
import webapp2
from webapp2_extras import sessions

from rosefire import RosefireTokenVerifier 


# from handlers.base_handlers import BaseHandler
#
ROSEFIRE_SECRET ="J0rh5xi1IPlzHJiHJCX3"

def __init_jinja_env():
    jenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols", "jinja2.ext.with_"],
        autoescape=True)
    # Example of a Jinja filter (useful for formatting data sometimes)
    #   jenv.filters["time_and_date_format"] = date_utils.time_and_date_format
    return jenv

jinja_env = __init_jinja_env()

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

class MainHandler(BaseHandler):
    def get(self):
        # A basic template could just send text out the response stream, but we use Jinja
        # self.response.write("Hello world!")
        template = jinja_env.get_template("templates/base_page.html")
        
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"])
          self.response.out.write(template.render({"user_info": user_info}))
        else:
          self.response.out.write(template.render())

class LoginHandler(BaseHandler):
    def get(self):
        if "user_info" not in self.session:
            token = self.request.get('token')
            auth_data = RosefireTokenVerifier(ROSEFIRE_SECRET).verify(token)
            user_info = {"name": auth_data.name,
                         "username": auth_data.username,
                         "email": auth_data.email,
                         "role": auth_data.group}
            self.session["user_info"] = json.dumps(user_info)
        self.redirect(uri="/")

class LogoutHandler(BaseHandler):
    def get(self):
        del self.session["user_info"]
        self.redirect(uri="/")

class ProfileHandler(BaseHandler):
    def get(self):
        template = jinja_env.get_template("templates/profile_page.html")
        
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"])
          self.response.out.write(template.render({"user_info": user_info}))
        else:
          self.response.out.write(template.render())
    
config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': 'J0rh5xi1IPlzHJiHJCX3',
}

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/login', LoginHandler),
    ('/logout', LogoutHandler),
    ('/profile', ProfileHandler)
], config=config, debug=True)