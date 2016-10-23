import webapp2

import main


class ListingHandler(webapp2.RequestHandler):
    def get(self):
        template = main.jinja_env.get_template("templates/listing.html")
        self.response.out.write(template.render())
