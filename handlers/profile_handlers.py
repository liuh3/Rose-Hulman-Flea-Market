import json

from handlers import base_handlers
import main


class ProfileHandler(base_handlers.BaseHandler):
    def get(self):
        template = main.jinja_env.get_template("templates/profile_page.html")
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"])
          self.response.out.write(template.render({"user_info": user_info}))
        else:
          self.response.out.write(template.render())

      