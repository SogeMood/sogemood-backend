from sogemood.messages.organisationMessage import UserMessage


class UserConverter():
    def convert_user(self, userModel):
        return UserMessage(
            name=userModel.name,
            mail=userModel.key.id(),
            active=userModel.active
        )

