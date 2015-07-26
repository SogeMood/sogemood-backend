__author__ = 'mwerlen'

from protorpc import messages


class OrganisationMessage(messages.Message):
    """Greeting that stores a message."""
    name = messages.StringField(1)


class OrganisationCollectionMessage(messages.Message):
    """Collection of Greetings."""
    items = messages.MessageField(OrganisationMessage, 1, repeated=True)


ORGANISATIONS_SAMPLE = OrganisationCollectionMessage(items=[
    OrganisationMessage(name="Sogelink"),
    OrganisationMessage(name="SQLI"),
    OrganisationMessage(name="Zenika"),
])
