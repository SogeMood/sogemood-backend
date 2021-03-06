import uuid

import endpoints
from protorpc import message_types
from protorpc import remote
from protorpc import messages

from google.appengine.ext import ndb

from sogemood.api.securedApi import secured_api
from sogemood.api.secured.converters.organisation_converter import OrganisationConverter
from sogemood.messages import organisationMessage
from sogemood.model.organisation import Organisation
from sogemood.model.team import Team
from sogemood.model.sogemooduser import SogeMoodUser


@secured_api.api_class(resource_name='organisation', path='organisations')
class OrganisationsApi(remote.Service):
    """
    Organisations API
    """

    @endpoints.method(message_types.VoidMessage, organisationMessage.OrganisationCollectionMessage,
                      http_method='GET',
                      name='organisation.list')
    def list_my_organisation(self, unused_request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException()
        my_organisations = Organisation.query(Organisation.admins_mail == current_user.email()).fetch()
        return OrganisationConverter().convert_organisation_collection(my_organisations)

    @endpoints.method(organisationMessage.CreateOrganisationMessage, organisationMessage.OrganisationMessage,
                      http_method='POST',
                      name='organisation.create')
    def add_organisation(self, request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException(message="Organisation creation is reserved to admins")
            # Check organisation code unicity
        if Organisation.get_by_id(request.code) is not None:
            raise endpoints.ConflictException(message="Code already attributed")
        organisation = Organisation(
            name=request.name,
            id=request.code,
            admins_mail=[current_user.email()]
        )
        organisation.put()
        return OrganisationConverter().convert_organisation(organisation)

    ADD_TEAM_RESOURCE = endpoints.ResourceContainer(organisationMessage.CreateTeamMessage,
                                                    code_organisation=messages.StringField(2, required=True))

    @endpoints.method(ADD_TEAM_RESOURCE, organisationMessage.TeamMessage,
                      path='{code_organisation}', http_method='POST',
                      name='team.add')
    def add_team(self, request):
        current_user = endpoints.get_current_user()
        organisation = Organisation.get_by_id(request.code_organisation)
        if current_user is None or current_user.email() not in organisation.admins_mail:
            raise endpoints.UnauthorizedException(message="Team creation is reserved to admins")
        team = Team(
            name=request.name,
            parent=organisation.key
        )
        team.put()
        organisation.teams.append(team.key)
        organisation.put()
        return OrganisationConverter().convert_team(team)

    LIST_TEAM_RESOURCE = endpoints.ResourceContainer(message_types.VoidMessage,
                                                     code_organisation=messages.StringField(2, required=True))

    @endpoints.method(LIST_TEAM_RESOURCE, organisationMessage.TeamCollectionMessage,
                      path='{code_organisation}/teams', http_method='GET',
                      name='team.list')
    def list_teams(self, request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException()
        organisation = Organisation.get_by_id(request.code_organisation)
        if organisation is None:
            raise endpoints.BadRequestException("Organisation %s does not exists" % request.code_organisation)
        if current_user.email() not in organisation.admins_mail:
            teams = Team.query(Team.users_mails == current_user.email(), ancestor=organisation.key).fetch()
        else:
            teams = Team.query(ancestor=organisation.key).fetch()
        return OrganisationConverter().convert_team_collection(teams)

    ADD_USER_RESOURCE = endpoints.ResourceContainer(organisationMessage.AddUserMessage,
                                                    code_organisation=messages.StringField(3, required=True),
                                                    team_id=messages.IntegerField(4, required=True))

    @endpoints.method(ADD_USER_RESOURCE, organisationMessage.TeamMessage,
                      path='{code_organisation}/teams/{team_id}', http_method='POST',
                      name='team.add_user')
    def add_member_to_team(self, request):
        if request.mail is None:
            raise endpoints.BadRequestException(message="User's email is mandatory")
        team = Team.get_by_id(request.team_id, parent=ndb.Key(Organisation, request.code_organisation))
        if team is None:
            raise endpoints.BadRequestException(message="No such team")
        team.users_mail.append(request.mail)
        team.put()
        return OrganisationConverter().convert_team(team)
