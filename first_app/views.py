import pathlib
import os
from datetime import datetime

from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from first_app.forms import UserCreationForm
from first_app.view_utils import create_custom_user
from django.conf import settings
from bson import json_util
import simplejson as json 

# Create your views here.


@api_view()
def home_page(request):
    """
    some docstring
    """
    return Response({"message": "Welcome!!!", "timestamp": datetime.now()})


@api_view()
def get_star_war_api_data(request):
    import requests
    from rest_framework import status

    url = "https://swapi.dev/api/films/"
    response = requests.get(url)
    if response.status_code not in [200, 201]:
        return Response({"error": "Failed to fetch details", "reason": response.text})
    return Response(response.json())


def redirect_url(request):
    """
    Just redirect to home page"""
    print(request.META.get("HTTP_REFERER"))
    return HttpResponseRedirect(reverse("homepage"))


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if not pathlib.Path("logged_details").exists():
            os.mkdir("logged_details")
        if form.is_valid():
            data = form.cleaned_data
            create_custom_user(data["username"], data["email"], data["password"])
            with open("logged_details/signed_users.txt", "a", encoding="utf-8") as f:
                f.write(f"{data['username']} => {data['email']} \n")

            return HttpResponseRedirect(reverse("homepage"))
        else:
            return JsonResponse(form.errors, status=400)
    else:
        form = UserCreationForm()
    return render(request, "create_user.html", {"form": form})


@api_view(["POST"])
def store_user_fav(request):
    request_data = request.data
    collection = settings.DJANGO_DOCKER["user_fav"]
    result = collection.insert_one(request_data)
    return Response({"message": "Successfully stored", 
    "id": str(result.inserted_id)})


@api_view(["GET"])
def get_fav_list(request):
    collection = settings.DJANGO_DOCKER["user_fav"]
    print(settings.DJANGO_DOCKER["user_fav"])
    result = json.loads(json_util.dumps(collection.find()))
    return Response({"message": "Successfully fetched", "result": result})
