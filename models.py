from google.appengine.ext import ndb

class User(ndb.Model):
  name = ndb.StringProperty()
  rose_username = ndb.StringProperty()
  phone_number = ndb.StringProperty()
  liked_item = ndb.KeyProperty(repeated=True)

class Item(ndb.Model):
  name = ndb.StringProperty(default="Item Name")
  description = ndb.TextProperty()
  price = ndb.FloatProperty()
  media_blob_key = ndb.BlobKeyProperty()
  posted_date = ndb.DateTimeProperty(auto_now=True)
  seller_key = ndb.KeyProperty()
  last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
  
class Comment(ndb.Model):
  content = ndb.StringProperty()
  author_key = ndb.KeyProperty();
  last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
  
    