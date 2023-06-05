import uuid
import random

from django.contrib.auth import logout, login
from django.shortcuts import redirect, render
from methodism import generate_key, code_decoder

from base.helper import check_otp
from dashboard.models.auth import Otp, User


def sign_in(requests):
    if not requests.user.is_anonymous:
        return redirect('dash_home')
    ctx = {}
    if requests.POST:
        password = requests.POST.get('pass')

        user = User.objects.filter(email='admin').first()
        if not user:
            ctx["error"] = True
            return render(requests, 'dashboard/auth/login.html', ctx)

        if not user.check_password(password):
            ctx["error"] = True
            return render(requests, 'dashboard/auth/login.html', ctx)

        otp = random.randint(100000, 999999)
        code = generate_key(50) + "$" + str(otp) + "$" + uuid.uuid4().__str__()
        hashed = code_decoder(code)
        requests.session['otp'] = otp

        root = Otp.objects.create(
            key=hashed,
            email='admin',
            extra={},
            step="sms-send",
            by=1
        )
        root.save()
        requests.session['token'] = hashed
        requests.session['st'] = 'otp'
        return redirect('otp')

    return render(requests, 'dashboard/auth/login.html', ctx)


def sign_out(requests, conf=False):
    if requests.user.is_anonymous:
        return redirect("sign-in")

    if not conf:
        return render(requests, "dashboard/auth/conf_out.html")

    logout(requests)

    return redirect("sign-in")


def otp(requests, status=None):
    if not requests.session.get('token'):
        return redirect('sign-in')
    if status == 1:
        otp = random.randint(100000, 999999)
        code = generate_key(50) + "$" + str(otp) + "$" + uuid.uuid4().__str__()
        hashed = code_decoder(code)
        requests.session['otp'] = otp
        last = Otp.objects.filter(key=requests.session['token']).first()
        Otp.objects.create(
            key=hashed,
            email=last.email,
            extra={},
            step="sms-send",
            by=last.by
        )
        requests.session['token'] = hashed
        requests.session['st'] = 'otp'
        return redirect('otp')

    if requests.session['st'] == 'otp' and requests.POST:
        code = "".join(x for x in requests.POST.getlist('otp'))
        otp = Otp.objects.filter(key=requests.session['token']).first()
        ctx = check_otp(otp, code)
        ctx.update({
            "hide": otp.email[-4:-2] + " " + otp.email[-2:]
        })
        if 'status' not in ctx:
            return render(requests, 'dashboard/auth/step-one.html', ctx)

        if otp.by == 1:
            user = User.objects.get(email=otp.email)
            login(requests, user)
            del requests.session['token']
            del requests.session['st']
            return redirect('dash_home')

    requests.session['st'] = 'otp'
    return render(requests, 'dashboard/auth/step-one.html')
