from django.urls import path
from first_app.views import home_page, redirect_url, create_user


urlpatterns = [
    path("", home_page, name="homepage"),
    path("redirect/", redirect_url, name="redirect"),
    path("create-user/", create_user, name="create_user")
]
