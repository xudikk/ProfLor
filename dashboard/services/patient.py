from django.shortcuts import render, redirect


def patients(requets, pk=None):
    ctx = {

    }
    return render(requets, 'dashboard/patient.html', ctx)
