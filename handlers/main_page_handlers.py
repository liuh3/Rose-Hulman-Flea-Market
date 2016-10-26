import json
import logging

import webapp2
from webapp2_extras import sessions

from handlers import base_handlers
import main
from rosefire import RosefireTokenVerifier
import utils


ROSEFIRE_SECRET ="J0rh5xi1IPlzHJiHJCX3"

class MainHandler(base_handlers.BaseHandler):
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

class LoginHandler(base_handlers.BaseHandler):
    def get(self):
        if "user_info" not in self.session:
            token = self.request.get('token')
            auth_data = RosefireTokenVerifier(ROSEFIRE_SECRET).verify(token)
            user_info = {"name": auth_data.name,
                         "username": auth_data.username,
                         "email": auth_data.email,
                         "role": auth_data.group,
                         "liked_items": [],
                         "posted_items": []}
            self.session["user_info"] = json.dumps(user_info)
        self.redirect(uri="/")

class LogoutHandler(base_handlers.BaseHandler):
    def get(self):
        del self.session["user_info"]
        self.redirect(uri="/")
