from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.



@login_required(login_url='sign-in')
def index(request):

    ctx = {}
    return render(request, 'dashboard/pages/index.html', ctx)


