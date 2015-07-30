__author__ = 'mwerlen'

from userMessage import *


class CreateOrganisationMessage(messages.Message):
    name = messages.StringField(1, required=True)
    code = messages.StringField(2, required=True)


class CreateTeamMessage(messages.Message):
    name = messages.StringField(1, required=True)


class AddUserMessage(messages.Message):
    mail = messages.StringField(1, required=True)


class TeamMessage(messages.Message):
    name = messages.StringField(1)
    users = messages.StringField(2, repeated=True)
    id = messages.IntegerField(3)


class TeamCollectionMessage(messages.Message):
    teams = messages.MessageField(TeamMessage, 1, repeated=True)


class OrganisationMessage(messages.Message):
    name = messages.StringField(1)
    teams = messages.MessageField(TeamMessage, 2, repeated=True)
    admins = messages.StringField(3, repeated=True)


class OrganisationCollectionMessage(messages.Message):
    organisations = messages.MessageField(OrganisationMessage, 1, repeated=True)
