import json
import logging

import webapp2

import main


class DetailItemHandler(webapp2.RequestHandler):
    def get(self):
        entity = self.request.get('entity')
        logging.info("Entity : "+entity)

        template = main.jinja_env.get_template("templates/detail_item_page.html")
        self.response.out.write(template.render({}))

        logging.info("CLICK")