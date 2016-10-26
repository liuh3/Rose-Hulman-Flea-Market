import webapp2

import main
import utils


class DetailItemHandler(webapp2.RequestHandler):
    def post(self):
        if self.request.get('item-entity-key'):
            entityKey = self.request.get('item-entity-key')
            itemToDisplay = utils.get_item_with_key(entityKey)
            
            template = main.jinja_env.get_template("templates/detail_item_page.html")
            self.response.out.write(template.render({"item" : itemToDisplay}))
        else:
            self.response.out.write(template.render({}))
