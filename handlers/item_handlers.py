from datetime import datetime
import json
import logging

from google.appengine.ext import ndb
import webapp2

from handlers import base_handlers
import main
from models import Comment
import ndb_utils


class DetailItemHandler(base_handlers.BaseHandler):
  def get(self):
    item_key = ndb.Key(urlsafe=self.request.get('item-entity-key'))
    template = main.jinja_env.get_template("templates/detail_item_page.html")
    itemToDisplay = item_key.get()
    comments = ndb_utils.get_comment_with_item_key(item_key)

    if "user_info" in self.session:
      user_info = json.loads(self.session["user_info"]) 
      is_seller = ndb_utils.get_parent_key(user_info) == itemToDisplay.seller_key
      user = ndb_utils.get_user_with_username(user_info['username'])
      already_liked = item_key in user.liked_item
      logging.info(already_liked)
      self.response.out.write(template.render({'user_info': user_info,
                                             "item" : itemToDisplay,
                                             "is_seller": is_seller,
                                             "already_liked": already_liked,
                                             "comments": comments}))
    else:
      self.response.out.write(template.render({"item": itemToDisplay}))

class CommentHandler(base_handlers.BaseHandler):
    def post(self):
      item_key = ndb.Key(urlsafe=self.request.get('item-entity-key'))
      logging.info(item_key)
      logging.info(item_key.get())
      comment = Comment(parent=item_key)

      if "user_info" in self.session:
        user_info = json.loads(self.session["user_info"])
        comment.author_key = ndb_utils.get_parent_key(user_info)
        comment.author_username = user_info['username']
      comment.content = self.request.get('content')
      comment.put()
      self.redirect(self.request.referer)    

class AddLikedItemHandler(base_handlers.BaseHandler):
  def post(self):
    item_key = ndb.Key(urlsafe=self.request.get('item-entity-key'))
    if "user_info" in self.session:
      user_info = json.loads(self.session["user_info"])
      user = ndb_utils.get_user_with_username(user_info['username'])
      if item_key not in user.liked_item:
        user.liked_item.append(item_key)
      else:
        user.liked_item.remove(item_key)
      user.put()
      self.redirect(self.request.referer)
