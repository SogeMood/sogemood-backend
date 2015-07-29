__author__ = 'mwerlen'

from protorpc import messages


class CreateOrganisationMessage(messages.Message):
    name = messages.StringField(1, required=True)
    code = messages.StringField(2, required=True)


class CreateTeamOrganisation(messages.Message):
    name = messages.StringField(1, required=True)


class UserMessage(messages.Message):
    name = messages.StringField(1)
    mail = messages.StringField(2)
    active = messages.BooleanField(3)


class TeamMessage(messages.Message):
    name = messages.StringField(1)
    users = messages.MessageField(UserMessage, 2, repeated=True)


class TeamCollectionMessage(messages.Message):
    teams = messages.MessageField(TeamMessage, 1, repeated=True)


class OrganisationMessage(messages.Message):
    name = messages.StringField(1)
    teams = messages.MessageField(TeamMessage, 2, repeated=True)
    admins = messages.StringField(3, repeated=True)


class OrganisationCollectionMessage(messages.Message):
    organisations = messages.MessageField(OrganisationMessage, 1, repeated=True)
