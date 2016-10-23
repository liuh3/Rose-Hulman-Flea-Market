from google.appengine.ext import ndb

class User(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    rose_username = ndb.StringProperty()
    image_url = ndb.StringProperty()
    phone_number = ndb.StringProperty()
    liked_item = ndb.KeyProperty(repeated=True, kind='Item')
    posted_item = ndb.KeyProperty(repeated=True, kind='Item')

class Item(ndb.Model):
    name = ndb.StringProperty(default="Item Name")
    description = ndb.TextProperty()
    price = ndb.FloatProperty()
    image_url = ndb.StringProperty()
    seller_key =  ndb.KeyProperty(kind=User)
    posted_date = ndb.DateTimeProperty(auto_now=True)
    
class Comment(ndb.Model):
    message = ndb.StringProperty()
    author_key = ndb.KeyProperty(kind=User)
    