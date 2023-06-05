from django.shortcuts import render

# Create your views here.
from dashboard.models import Contact


def index(requests):

    ctx = {
        "contact": Contact.objects.filter().first()
    }

    return render(requests, 'site/pages/index.html', ctx)

