from datetime import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from first_app.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from first_app.view_utils import create_custom_user
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
        import pathlib
        import os
        if not pathlib.Path("logged_details").exists():
            os.mkdir("logged_details")
        if form.is_valid():
            data = form.cleaned_data
            create_custom_user(data['user_name'],
                               data['email'], data['password'])
            with open("logged_details/signed_users.txt", "a", encoding="utf-8") as f:
                f.write(f"{data['user_name']} => {data['email']} \n")

            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = UserCreationForm()
    return render(request, 'create_user.html', {'form': form})
