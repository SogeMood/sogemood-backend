__author__ = 'mwerlen'

from google.appengine.ext import ndb

import sogemooduser
import team
import organisation


class Mood(ndb.Model):
    user = ndb.KeyProperty(sogemooduser.SogeMoodUser)
    team = ndb.KeyProperty(team.Team)
    organisation = ndb.KeyProperty(organisation.Organisation)

    date = ndb.DateProperty()
    modification_date = ndb.DateTimeProperty()

    mood = ndb.IntegerProperty()
