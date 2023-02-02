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
# Create your views here.


@api_view()
def home_page(request):
    """
    some docstring 
    """
    return Response({
        "message": "Welcome",
        "timestamp": datetime.now()
    })


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
            create_custom_user(data['username'],
                               data['email'], data['password'])
            with open("logged_details/signed_users.txt", "a", encoding="utf-8") as f:
                f.write(f"{data['username']} => {data['email']} \n")

            return HttpResponseRedirect(reverse('homepage'))
        else:
            return JsonResponse(form.errors, status=400)
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})
