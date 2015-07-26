"""

    Une API exemple

"""

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

from sogemood.messages import greetings
from sogemood.api.publicApi import public_api

package = 'SogeMood'


@public_api.api_class(resource_name='helloWorld', path='hello')
class HelloWorldApi(remote.Service):
    """Helloworld API v1."""

    @endpoints.method(message_types.VoidMessage, greetings.GreetingCollection, path='hellogreeting', http_method='GET',
                      name='greetings.listGreeting')
    def greetings_list(self, unused_request):
        return greetings.STORED_GREETINGS

    ID_RESOURCE = endpoints.ResourceContainer(message_types.VoidMessage,
                                              id=messages.IntegerField(1, variant=messages.Variant.INT32))

    @endpoints.method(ID_RESOURCE, greetings.Greeting, path='hellogreeting/{id}', http_method='GET',
                      name='greetings.getGreeting')
    def greeting_get(self, request):
        try:
            return greetings.STORED_GREETINGS.items[request.id]
        except (IndexError, TypeError):
            raise endpoints.NotFoundException('Greeting %s not found.' % (request.id,))

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(greetings.Greeting,
                                                           times=messages.IntegerField(2,
                                                                                       variant=messages.Variant.INT32,
                                                                                       required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE, greetings.Greeting,
                      path='hellogreeting/{times}', http_method='POST',
                      name='greetings.multiply')
    def greetings_multiply(self, request):
        return greetings.Greeting(message=request.message * request.times)

    @endpoints.method(message_types.VoidMessage, greetings.Greeting,
                      path='authed', http_method='POST',
                      name='greetings.authed')
    def greeting_authed(self, request):
        current_user = endpoints.get_current_user()
        email = (current_user.nickname() if current_user is not None
                 else 'Anonymous')
        return greetings.Greeting(message='hello %s' % (email,))
