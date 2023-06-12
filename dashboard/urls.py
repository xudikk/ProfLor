from django.urls import path

from dashboard.services.auth import sign_in, sign_out, otp
from .services.auto import auto_form, gets, auto_del
from .services.contact import contact
from .services.patients import patients, patient_form, patient_del

from .views import index

urlpatterns = [
    # auth
    path("", index, name="home"),
    path("auth/", sign_in, name="sign-in"),
    path("auth/logout/", sign_out, name="sign-out"),
    path("auth/logout/<conf>/", sign_out, name="sign-out-conf"),
    #
    # # auth-otp
    path("auth/otp/", otp, name="otp"),
    path("auth/otp/<int:status>/", otp, name="otp-new"),

    # # pages
    path("contact/", contact, name="dashboard-contact"),

    # auto
    path("auto/<key>/", gets, name="dashboard-auto-list"),
    path("auto/<key>/<int:pk>/", gets, name="dashboard-auto-detail"),
    path("auto/<key>/add/", auto_form, name="dashboard-auto-add"),
    path("auto/<key>/edit/<int:pk>/", auto_form, name="dashboard-auto-edit"),
    path("auto/<key>/del/<int:pk>/", auto_del, name="dashboard-auto-delete"),

    # patient
    path("patient/", patients, name="dashboard-patient-list"),
    path("patient/<int:pk>/", patients, name="dashboard-patient-detail"),
    path("patient/add/", patient_form, name="dashboard-patient-add"),
    path("patient/edit/<int:pk>/", patient_form, name="dashboard-patient-edit"),
    path("patient/del/<int:pk>/", patient_del, name="dashboard-patient-delete"),
]


