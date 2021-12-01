from django.shortcuts import render

from svix.api import Svix, ApplicationIn


def index(request):

    svix = Svix("AUTH_TOKEN")
    app = svix.application.create(ApplicationIn(name="Application name"))

    # good overview https://api.svix.com/docs#section/Introduction
    return render(request, "index.html")
