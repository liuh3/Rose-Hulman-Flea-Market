import json
import logging

from handlers import base_handlers
import main
import utils

class LikedHandler(base_handlers.BaseHandler):
  def get(self):
    template = main.jinja_env.get_template("templates/posted_list.html")
    if "user_info" in self.session:
      user_info = json.loads(self.session["user_info"]) 
      user = utils.get_user_with_username(user_info['username'])
      liked_item_keys = user.liked_item
      logging.info(liked_item_keys)
      liked_items = []
      for item in liked_item_keys:
        liked_items.append(item.get())
      self.response.out.write(template.render({"user_info": user_info, "items": liked_items}))
      

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
   
  
