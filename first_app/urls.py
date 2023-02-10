from django.urls import path
from first_app.views import home_page, redirect_url, get_star_war_api_data, create_user


urlpatterns = [
    path("", home_page, name="homepage"),
    path("redirect/", redirect_url, name="redirect"),
    path("star-war/", get_star_war_api_data, name="star war"),
    path("create-user/", create_user, name="create_user")
]
