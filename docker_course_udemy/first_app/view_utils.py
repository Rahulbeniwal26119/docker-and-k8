from django.contrib.auth import get_user_model

user_model = get_user_model()


def create_custom_user(user_name, email, password, is_admin=False):
    user = user_model(
        username=user_name, email=email,
        staff_member=is_admin
    )
    user.set_password(password)
    user.save()
    return user 