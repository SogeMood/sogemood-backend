from google.appengine.ext import ndb

import sogemooduser


class Team(ndb.Model):
    name = ndb.StringProperty()
    users_mail = ndb.StringProperty(repeated=True)
