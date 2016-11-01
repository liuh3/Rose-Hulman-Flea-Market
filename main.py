
import os

import jinja2
import webapp2

from handlers import insert_handlers, main_page_handlers, \
  profile_handlers, blob_handlers, listing_handlers, item_handlers


def __init_jinja_env():
    jenv = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=["jinja2.ext.do", "jinja2.ext.loopcontrols", "jinja2.ext.with_"],
        autoescape=True)
    # Example of a Jinja filter (useful for formatting data sometimes)
    #   jenv.filters["time_and_date_format"] = date_utils.time_and_date_format
    return jenv

jinja_env = __init_jinja_env()


config = {}
config['webapp2_extras.sessions'] = {
    # This key is used to encrypt your sessions
    'secret_key': 'J0rh5xi1IPlzHJiHJCX3',
}

app = webapp2.WSGIApplication([
    ('/', main_page_handlers.MainHandler),
    ('/img/([^/]+)?', blob_handlers.BlobServer),
    ('/login', main_page_handlers.LoginHandler),
    ('/logout', main_page_handlers.LogoutHandler),
    ('/view-item', item_handlers.DetailItemHandler),
    ('/insert-user', insert_handlers.InsertUserHandler),
    ('/insert-item', insert_handlers.InsertItemHandler),
    ('/add-liked-item', item_handlers.AddLikedItemHandler),
    ('/delete-item', insert_handlers.DeleteItemHandler),
    ('/posted-items', listing_handlers.PostedHandler),
    ('/liked-items', listing_handlers.LikedHandler),
    ('/profile', profile_handlers.ProfileHandler)
], config=config, debug=True)
