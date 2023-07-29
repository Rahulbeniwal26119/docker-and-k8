from django.urls import path
from first_app.views import (
    home_page,
    redirect_url,
    get_star_war_api_data,
    create_user,
    get_fav_list,
    store_user_fav,
    exit_server
)


urlpatterns = [
    path("", home_page, name="homepage"),
    path("exit/", exit_server, name="exit"),
    path("redirect/", redirect_url, name="redirect"),
    path("star-war/", get_star_war_api_data, name="star war"),
    path("create-user/", create_user, name="create_user"),
    path("fav-list/", get_fav_list, name="get_fav_list"),
    path("store-fav/", store_user_fav, name="store_user_fav")
]
