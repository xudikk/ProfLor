from django.shortcuts import render

# Create your views here.


def index(requests):

    return render(requests, 'site/pages/index.html')

