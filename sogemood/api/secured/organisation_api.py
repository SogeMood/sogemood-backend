import endpoints
from protorpc import message_types
from protorpc import remote

from sogemood.api.securedApi import secured_api
from sogemood.messages import organisationMessage


@secured_api.api_class(resource_name='organisation', path='organisations')
class OrganisationsApi(remote.Service):
    """
    Organisations API
    """

    @endpoints.method(message_types.VoidMessage, organisationMessage.OrganisationCollectionMessage,
                      path='', http_method='GET',
                      name='list')
    def organisation_list(self, unused_request):
        return organisationMessage.ORGANISATIONS_SAMPLE
