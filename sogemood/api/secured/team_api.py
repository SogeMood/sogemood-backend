import endpoints
from protorpc import message_types
from protorpc import remote

from sogemood.messages import organisationMessage
from sogemood.api.securedApi import secured_api

@secured_api.api_class(resource_name='team', path='teams')
class TeamsApi(remote.Service):
    """
    Team API
    """

    @endpoints.method(message_types.VoidMessage, organisationMessage.OrganisationCollectionMessage,
                      path='', http_method='GET',
                      name='list')
    def team_list(self, unused_request):
        return organisationMessage.ORGANISATIONS_SAMPLE
