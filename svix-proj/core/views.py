import os
import json 

from django.shortcuts import render, redirect

from svix.api import Svix, ApplicationIn, Application, MessageIn

# app id to use
app_id = "Svix3"

def index(request):
    
    # setup api
    svix = Svix(os.environ.get('SVIX_API_KEY'))
    
    
    # # good overview https://api.svix.com/docs#section/Introduction
    # # an "application" refers to a user application
    # # i.e., where we will be sending webhooks
    # app = svix.application.create(ApplicationIn(name=app_id, uid=app_id))

    
    # # sending messages
    # # https://www.svix.com/guides/sending/send-webhooks-with-svix-cli/
    # svix.message.create(
    # app_id,
    # MessageIn(
    #     event_type="invoice.paid",
    #     event_id="djydntynd",
    #     payload={
    #         "id": "djydj",
    #         "status": "paid",
    #         "attempt": 2
    #         }
    #     )
    # )
    
    # ui dashboard
    dashboard_access_out = svix.authentication.dashboard_access(app_id)
    
    # redirect to dashboard
    # NOTE: on initial usage you will have to setup a webhook endpoint
    return redirect(dashboard_access_out.url)
