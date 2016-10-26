import json
import logging

from handlers import base_handlers
import main
import utils


class PostedHandler(base_handlers.BaseHandler):
  def get(self):
    template = main.jinja_env.get_template("templates/posted_list.html")
    if "user_info" in self.session:
      user_info = json.loads(self.session["user_info"])
      items = utils.get_posted_items(user_info)
      logging.info(items)
      self.response.out.write(template.render({"user_info": user_info, "items": items}))
    else:
      self.response.out.write(template.render({}))
   
  
