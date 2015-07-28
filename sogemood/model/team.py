from google.appengine.ext import ndb

import user


class Team(ndb.Model):
    name = ndb.StringProperty()
    users = ndb.StructuredProperty(user.User, repeated=True)
