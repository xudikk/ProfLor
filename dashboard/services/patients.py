import datetime

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from base.texts import BEMOR
from dashboard.models import Patients, Diagnoz
from dashboard.forms import PatientsForm, DiagnozForm


@login_required(login_url='sign-in')
def patients(requests, pk=None, status=None, diag_id=None):
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
        if status == 1:
            diag = Diagnoz.objects.filter(pk=diag_id).first()
            form = DiagnozForm(instance=diag)
            if requests.POST:
                if not diag:
                    diag = Diagnoz()
                diag.patient = root
                diag.name = requests.POST.get('name', diag.name)
                diag.save()
                return redirect('dashboard-patient-detail', pk=pk)

            ctx['form'] = form
            ctx['diag_status'] = 'form'

        return render(requests, f'dashboard/pages/patient.html', ctx)

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
        root = form.save()

        return redirect('dashboard-patient-detail', pk=root.id)

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


@login_required(login_url='sign-in')
def change_lan(requests, pk,  lang='kr'):
    if lang in ['uz', 'ru', 'kr']:
        requests.session['lang'] = lang
    return redirect('screen-page', pk=pk)


@login_required(login_url='sign-in')
def generator_screen(requests, pk):
    root = Diagnoz.objects.filter(id=pk).first()
    if not root:
        ctx = {"error": 404}
        return render(requests, f'dashboard/base.html', ctx)

    bemor = {}
    for i in BEMOR.keys():
        bemor[i] = BEMOR[i][requests.session.get('lang', 'kr')]

    ctx = {
        "bemor": bemor,
        "root": root,
        "date": datetime.datetime.today()
    }

    return render(requests, f'dashboard/pages/bemor.html', ctx)
