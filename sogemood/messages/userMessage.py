__author__ = 'mwerlen'

from protorpc import messages

class UserMessage(messages.Message):
    name = messages.StringField(1)
    mail = messages.StringField(2)
    active = messages.BooleanField(3)

class Register(messages.Message):
    name = messages.StringField(1)