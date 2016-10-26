from google.appengine.ext import ndb

class Item(ndb.Model):
    name = ndb.StringProperty(default="Item Name")
    description = ndb.TextProperty()
    price = ndb.FloatProperty()
    media_blob_key = ndb.BlobKeyProperty()
    posted_date = ndb.DateTimeProperty(auto_now=True)
    seller_key = ndb.KeyProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    
class Comment(ndb.Model):
    message = ndb.StringProperty()
    author_key = ndb.KeyProperty();
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
  
    