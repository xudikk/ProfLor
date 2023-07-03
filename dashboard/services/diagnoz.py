from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from dashboard.models import Diagnoz, Suggests
from dashboard.forms import DiagnozForm, SuggestForm


@login_required(login_url='sign-in')
def diagnozs(requests, pk=None, status=None, suggest_id=None):
    if pk:
        root = Diagnoz.objects.filter(pk=pk).first()
        suggests = Suggests.objects.filter(diagnoz=root)
        if not root:
            return render(requests, 'dashboard/base.html', {'error': 404})

        ctx = {
            "pos": "one",
            'root': root,
        }
        if status == 1:
            suggest = Suggests.objects.filter(pk=suggest_id).first()
            form = SuggestForm(instance=suggest, diagnoz=root)
            if requests.POST:
                print(requests.POST)
                forms = SuggestForm(requests.POST, instance=suggest, diagnoz=root)
                forms.diagnoz = root
                if forms.is_valid():
                    forms.save()
                else:
                    print(forms.errors)

                # if not suggest:
                #     suggest = Suggests()
                # suggest.diagnoz = root
                # suggest.suggest = requests.POST.get('suggest', suggest.suggest)
                # suggest.tablet = requests.POST.get('tablet', suggest.tablet)
                # suggest.save()
                return redirect('dashboard-diags-detail', pk=pk)

            ctx['form'] = form
            ctx['suggest_status'] = 'form'
        ctx['suggests'] = suggests

    else:
        pagination = Diagnoz.objects.all().order_by('-pk')
        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list"
        }

    return render(requests, f'dashboard/pages/diags.html', ctx)


@login_required(login_url='sign-in')
def diagnoz_form(requests, pk=None):
    root = None
    if pk:
        root = Diagnoz.objects.filter(pk=pk).first()
        if not root:
            ctx = {"error": 404}
            return render(requests, f'dashboard/base.html', ctx)

    form = DiagnozForm(requests.POST or None, requests.FILES or None, instance=root)
    if form.is_valid():
        root = form.save()

        return redirect('dashboard-diags-detail', pk=root.id)

    ctx = {
        "form": form,
        "pos": 'form'
    }
    return render(requests, f'dashboard/pages/diags.html', ctx)


@login_required(login_url='sign-in')
def diagnoz_del(requests, pk):
    root = Diagnoz.objects.filter(pk=pk).first()
    if not root:
        ctx = {"error": 404}
        return render(requests, f'dashboard/pages/diags.html', ctx)
    root.delete()
    return redirect('dashboard-diags-list')




