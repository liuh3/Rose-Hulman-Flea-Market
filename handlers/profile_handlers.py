import json

from handlers import base_handlers
import main
import ndb_utils


class ProfileHandler(base_handlers.BaseHandler):
    def get(self):
        template = main.jinja_env.get_template("templates/profile_page.html")
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"])
          user_model = ndb_utils.get_user_with_username(user_info['username'])
          self.response.out.write(template.render({"user_info": user_info, "user_model": user_model}))
        else:
          self.response.out.write(template.render())
      