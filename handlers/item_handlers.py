import json
import logging

import webapp2

from handlers import base_handlers
import main
import utils


class DetailItemHandler(base_handlers.BaseHandler):
    def post(self):
      if self.request.get('item-entity-key'):
        template = main.jinja_env.get_template("templates/detail_item_page.html")
        entityKey = self.request.get('item-entity-key')
        itemToDisplay = utils.get_item_with_key(entityKey)
        if "user_info" in self.session:
          user_info = json.loads(self.session["user_info"]) 
          is_seller = utils.get_parent_key(user_info) == itemToDisplay.seller_key
          self.response.out.write(template.render({'user_info': user_info, "item" : itemToDisplay, "is_seller": is_seller}))
        else:
          self.response.out.write(template.render({"item" : itemToDisplay}))