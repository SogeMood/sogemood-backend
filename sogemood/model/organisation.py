__author__ = 'mwerlen'

from google.appengine.ext import ndb

import team


class Organisation(ndb.Model):
    # id is the organisation code
    name = ndb.StringProperty()
    admins_mail = ndb.StringProperty(repeated=True)
    teams = ndb.KeyProperty(team.Team, repeated=True)
