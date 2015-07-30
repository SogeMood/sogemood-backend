import uuid

import endpoints
from protorpc import message_types
from protorpc import remote

from sogemood.api.securedApi import secured_api
from sogemood.messages import organisationMessage, userMessage
from sogemood.model.sogemooduser import SogeMoodUser
from sogemood.api.secured.converters.user_converter import UserConverter


@secured_api.api_class(resource_name='user', path='users')
class UsersApi(remote.Service):
    """
        User API
    """

    @endpoints.method(message_types.VoidMessage, organisationMessage.UserMessage,
                      path="me", http_method='GET',
                      name='user.me')
    def get_me(self, unused_request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.BadRequestException()
        user = SogeMoodUser.get_by_id(current_user.email())
        if user is None:
            raise endpoints.UnauthorizedException(message="You're not a member yet, register to give a try")
        return UserConverter().convert_user(user)

    @endpoints.method(userMessage.Register, userMessage.UserMessage,
                      path="me", http_method='POST',
                      name='user.register')
    def register(self, register_message):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException
        user = SogeMoodUser.get_by_id(current_user.email())
        if user is None:
            user = SogeMoodUser(active=True, id=str(current_user.email()))
        user.name = register_message.name
        user.token = str(uuid.uuid4())
        user.put();
        return UserConverter().convert_user(user)
