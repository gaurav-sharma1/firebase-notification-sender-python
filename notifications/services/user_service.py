from notifications.models import AppUser, FCMToken

class UserService:

    @staticmethod
    def delete_user(user_id):
        user = AppUser.objects.filter(id=user_id).first()
        if not user:
            return False
        user.delete()
        return True

    def register_user_token(username: str, token: str) :
        user, _ = AppUser.objects.get_or_create(username=username)
        FCMToken.objects.get_or_create(user=user, token=token)
        return user

