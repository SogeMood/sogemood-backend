from  google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    mail = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty(required=False)
    token = ndb.StringProperty(required=True)
    active = ndb.BooleanProperty(required=True, default=True)
