import os
import json 

from django.shortcuts import render, redirect

from svix.api import Svix, ApplicationIn, Application, MessageIn


def index(request):
    svix = Svix(os.environ.get('SVIX_API_KEY'))
    # good overview https://api.svix.com/docs#section/Introduction
    
    # an "application" refers to a user application
    # i.e., where we will be sending webhooks
    # app = svix.application.create(ApplicationIn(name="SvixTest", uid="Svix1"))

    
    # sending messages
    svix.message.create(
    "Svix1",
    MessageIn(
        event_type="invoice.paid",
        event_id="evt_Wqb1k73rXprtTm7Qdlr38G",
        payload={
            "id": "invoice_WF7WtCLFFtd8ubcTgboSFNql",
            "status": "paid",
            "attempt": 2
            }
        )
    )
    
    # ui dashboard
    dashboard_access_out = svix.authentication.dashboard_access('Svix1')
    # print(dashboard_access_out)
    # decoded = json.loads(dashboard_access_out)
    return redirect(dashboard_access_out.url)
    return render(request, "index.html")
