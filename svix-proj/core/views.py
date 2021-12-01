import os

from django.shortcuts import render

from svix.api import Svix, ApplicationIn, Application, MessageIn


def index(request):
    svix = Svix(os.environ.get('SVIX_API_KEY'))
    # good overview https://api.svix.com/docs#section/Introduction
    
    # an "application" refers to a user application
    # i.e., where we will be sending webhooks
    app = svix.application.delete(Application() )

    
    # sending messages
    # svix.message.create(
    # "Svix-Test",
    # MessageIn(
    #     event_type="invoice.paid",
    #     event_id="evt_Wqb1k73rXprtTm7Qdlr38G",
    #     payload={
    #         "id": "invoice_WF7WtCLFFtd8ubcTgboSFNql",
    #         "status": "paid",
    #         "attempt": 2
    #         }
    #     )
    # )
    
    # ui dashboard
    # dashboard_access_out = svix.authentication.dashboard_access('6F9gtf')
    return render(request, "index.html")
