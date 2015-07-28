from  google.appengine.ext import ndb

class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    mail = ndb.StringProperty(required=True)
    token = ndb.StringProperty(required=True)
    active = ndb.BooleanProperty(required=True, default=True)
