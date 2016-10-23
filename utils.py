import logging

from google.appengine.ext import ndb

from models import Item


def get_parent_key(user):
  return ndb.Key("Entity", user['email'].lower())

def get_items():
  """ Gets all of the items and makes a key map for them. """
  items = Item.query().fetch()
  logging.info(items)

  return items
