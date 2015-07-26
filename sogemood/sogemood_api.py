"""Sogemood API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""

import endpoints
from sogemood.api.secured import organisation_api, team_api
from sogemood.api.public import helloworld_api

package = 'SogeMood'

APPLICATION = endpoints.api_server([
    #Public
    helloworld_api.HelloWorldApi,

    #Secured
    organisation_api.OrganisationsApi,
    team_api.TeamsApi
])
