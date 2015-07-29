from sogemood.messages.organisationMessage import OrganisationMessage, TeamMessage, UserMessage, \
    OrganisationCollectionMessage, TeamCollectionMessage


class OrganisationConverter():
    def convert_organisation_collection(self, organisations):
        return OrganisationCollectionMessage(
            organisations=map(self.convert_organisation, organisations)
        )

    def convert_organisation(self, organisationModel):
        message = OrganisationMessage(
            name=organisationModel.name,
            teams=map(self.convert_team, organisationModel.teams),
            admins=organisationModel.admins_mail
        )
        return message

    def convert_team_collection(self, teams):
        return TeamCollectionMessage(
            teams=map(self.convert_team, teams)
        )

    def convert_team(self, teamModel):
        message = TeamMessage(
            name=teamModel.name,
            users=map(self.convert_user, teamModel.users)
        )
        return message

    def convert_user(self, userModel):
        message = UserMessage(
            name=userModel.name,
            mail=userModel.mail,
            active=userModel.active
        )
