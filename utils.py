import logging

from google.appengine.ext import ndb

from models import Item

PARENT_KEY = ndb.Key("Entity", "item_root")

def get_parent_key(user):
  return ndb.Key("Entity", user['email'].lower())

def get_items():
  """ Gets all of the items and makes a key map for them. """
  items = Item.query(ancestor=PARENT_KEY).order(-Item.last_touch_date_time);

  return items
