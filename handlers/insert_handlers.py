import json
import logging

from google.appengine.ext import ndb
from google.appengine.ext.webapp import blobstore_handlers

from handlers import base_handlers
import main
from google.appengine.api import blobstore
from models import Item
import utils


PARENT_KEY = ndb.Key("Entity", "item_root")

class DeleteItemHandler(base_handlers.BaseHandler):
    def post(self):
      delete_item = ndb.Key(urlsafe=self.request.get('item-entity-key'))
      delete_item.delete()
      self.redirect('/')
  
class InsertItemHandler(base_handlers.BaseHandler, blobstore_handlers.BlobstoreUploadHandler):
    def get(self):
        template = main.jinja_env.get_template("templates/insert_item.html")
        urlsafe_entity_key = self.request.get('item-entity-key')
        logging.info(urlsafe_entity_key)
        if "user_info" in self.session:
            user_info = json.loads(self.session["user_info"])
            if len(urlsafe_entity_key) > 0:
              item_key = ndb.Key(urlsafe=urlsafe_entity_key)
              item = item_key.get()
              self.response.out.write(template.render({"user_info": user_info, "form_action": blobstore.create_upload_url('/insert-item'), "item": item}))
            else: 
              self.response.out.write(template.render({"user_info": user_info, "form_action": blobstore.create_upload_url('/insert-item') }))
        else:
            self.response.out.write(template.render())
    

    def post(self):
        user = json.loads(self.session["user_info"]);
        urlsafe_entity_key = self.request.get('item-entity-key')
        if len(urlsafe_entity_key) > 0:
          # Edit
          item_key = ndb.Key(urlsafe=urlsafe_entity_key)
          item = item_key.get()
          logging.info(item)
        else:
          #Add
          item = Item(parent=PARENT_KEY);
          item.seller_key = utils.get_parent_key(user);
          
        if self.get_uploads() and len(self.get_uploads()) == 1:
          logging.info("Received an image blob with this text message event.")
          media_blob = self.get_uploads()[0]
          item.media_blob_key = media_blob.key()
      
        item.name=self.request.get('item_name')
        item.image_url = self.request.get('image_url')
        item.price = float(self.request.get('item_price'))
        item.description = self.request.get('item_description')
        
        logging.info(item)
        item.put()
        self.redirect('/')