from google.appengine.ext import ndb


def get_parent_key(user):
  return ndb.Key("Entity", user['email'].lower())