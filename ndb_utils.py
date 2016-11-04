from google.appengine.ext import ndb

from models import Item, User, Comment


PARENT_KEY = ndb.Key("Entity", "item_root")
USER_PARENT_KEY = ndb.Key("Entity", "user_root")

def get_parent_key(user):
    return ndb.Key("Entity", user['email'].lower())

def contain_user(username):
  return User.query(User.rose_username==username).count() == 0

def get_user_with_username(username): 
  return User.query(ancestor=USER_PARENT_KEY).filter(User.rose_username==username).fetch()[0]

def get_user_with_email(user_email):
  return User.query(ancestor=USER_PARENT_KEY).filter(User.email==user_email).fetch()[0]

def get_items():
    """ Gets all of the items and makes a key map for them. """
    items = Item.query(ancestor=PARENT_KEY).order(-Item.last_touch_date_time);
    return items

def get_posted_items(user):
  user_key = get_parent_key(user)
  items = Item.query(Item.seller_key==user_key).order(-Item.last_touch_date_time);
  return items

def get_item_with_key(key_url_string):
  item_key = ndb.Key(urlsafe=key_url_string)
  return item_key.get()

def get_comment_with_item_key(item_key):
  comments = Comment.query(ancestor=item_key).order(-Item.last_touch_date_time)
  return comments
