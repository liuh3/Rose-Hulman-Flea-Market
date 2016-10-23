import json
import logging

from google.appengine.ext import ndb

from handlers import base_handlers
import main
from models import Item
import utils


class InsertItemHandler(base_handlers.BaseHandler):
    def get(self):
        template = main.jinja_env.get_template("templates/insert_item.html")
        if "user_info" in self.session:
            user_info = json.loads(self.session["user_info"])
            self.response.out.write(template.render({"user_info": user_info}))
        else:
            self.response.out.write(template.render())
    

    def post(self):
        user = json.loads(self.session["user_info"]);
        urlsafe_entity_key =  self.request.get('item_entity_key')
        if len(urlsafe_entity_key) > 0:
          # Edit
          item_key = ndb.Key(urlsafe=urlsafe_entity_key)
          item = item_key.get()
        else:
          #Add
          item = Item(parent=utils.get_parent_key(user));
       
#         item.seller_key = user
        item.name=self.request.get('item_name')
        item.image_url = self.request.get('image_url')
        item.price = float(self.request.get('item_price'))
        item.description = self.request.get('item_description')
        logging.info(item)
        item.put()
        self.redirect('/')