from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from dashboard.forms.contact import ContactForm
from dashboard.models import Contact


@login_required(login_url='sign-in')
def contact(requests):
    root = Contact.objects.filter().first()
    form = ContactForm(requests.POST or None, instance=root)

    ctx = {
        "root": root,
    }
    if form.is_valid():
        form.save()
        ctx['success'] = True

    ctx["form"] = form

    return render(requests, 'dashboard/pages/contact.html', ctx)
