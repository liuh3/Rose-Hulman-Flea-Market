import json
import logging

import webapp2
from webapp2_extras import sessions

import main
from rosefire import RosefireTokenVerifier
import utils


ROSEFIRE_SECRET ="J0rh5xi1IPlzHJiHJCX3"

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
        items = utils.get_items()
        template = main.jinja_env.get_template("templates/feed_list.html")
        
        if "user_info" in self.session:
            user_info = json.loads(self.session["user_info"])
            self.response.out.write(template.render({"user_info": user_info,"items":items}))
        else:
          self.response.out.write(template.render({"items":items}))

class DetailItemHandler(webapp2.RequestHandler):        
    def post(self):
        logging.info("here")
        if  self.request.get("item_entity_key"):
            logging.info("Key found")
    
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