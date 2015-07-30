from sogemood.messages.organisationMessage import OrganisationMessage, TeamMessage, OrganisationCollectionMessage, \
    TeamCollectionMessage


class OrganisationConverter():
    def convert_organisation_collection(self, organisations):
        return OrganisationCollectionMessage(
            organisations=map(self.convert_organisation, organisations)
        )

    def convert_organisation(self, organisationModel):
        message = OrganisationMessage(
            name=organisationModel.name,
            teams=map(self.convert_team_key, organisationModel.teams),
            admins=organisationModel.admins_mail
        )
        return message

    def convert_team_collection(self, teams):
        return TeamCollectionMessage(
            teams=map(self.convert_team, teams)
        )

    def convert_team(self, team_model):
        message = TeamMessage(
            name=team_model.name,
            users=team_model.users_mail,
            id=team_model.key.id()
        )
        return message

    def convert_team_key(self, team_key):
        team_model = team_key.get()
        message = TeamMessage(
            name=team_model.name,
            users=team_model.users_mail,
            id=team_model.key.id()
        )
        return message
