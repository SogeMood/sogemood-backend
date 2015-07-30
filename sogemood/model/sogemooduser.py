# noinspection PyPackageRequirements
from google.appengine.ext import ndb


class SogeMoodUser(ndb.Model):
    name = ndb.StringProperty(required=True)
    token = ndb.StringProperty(required=True)
    active = ndb.BooleanProperty(required=True, default=True)
