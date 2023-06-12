from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from dashboard.models import Patients, Diagnoz
from dashboard.forms import PatientsForm


@login_required(login_url='sign-in')
def patients(requests, pk=None):

    if pk:
        root = Patients.objects.filter(pk=pk).first()
        diags = Diagnoz.objects.filter(patient=root)
        if not root:
            return render(requests, 'dashboard/base.html', {'error': 404})

        ctx = {
            "pos": "one",
            'root': root,
            'diags': diags
        }
    else:
        pagination = Patients.objects.all().order_by('-pk')
        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list"
        }

    return render(requests, f'dashboard/pages/patient.html', ctx)


@login_required(login_url='sign-in')
def patient_form(requests, pk=None):
    root = None
    if pk:
        root = Patients.objects.filter(pk=pk).first()
        if not root:
            ctx = {"error": 404}
            return render(requests, f'dashboard/pages/patient.html', ctx)

    form = PatientsForm(requests.POST or None, requests.FILES or None, instance=root)
    if form.is_valid():
        form.save()
        return redirect('dashboard-patient-list')

    ctx = {
        "form": form,
        "pos": 'form'
    }
    return render(requests, f'dashboard/pages/patient.html', ctx)


@login_required(login_url='sign-in')
def patient_del(requests, pk):

    root = Patients.objects.filter(pk=pk).first()
    if not root:
        ctx = {"error": 404}
        return render(requests, f'dashboard/pages/patient.html', ctx)
    root.delete()
    return redirect('dashboard-patient-list')




