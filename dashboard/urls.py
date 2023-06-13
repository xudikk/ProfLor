from django.urls import path

from dashboard.services.auth import sign_in, sign_out, otp
from .services.auto import auto_form, gets, auto_del
from .services.contact import contact
from .services.patients import patients, patient_form, patient_del, generator_screen, change_lan
from .services.diagnoz import diagnoz_form, diagnoz_del, diagnozs

from .views import index

urlpatterns = [
    # auth
    path("", index, name="home"),
    path("auth/", sign_in, name="sign-in"),
    path("auth/logout/", sign_out, name="sign-out"),
    path("auth/logout/<conf>/", sign_out, name="sign-out-conf"),

    # auth-otp
    path("auth/otp/", otp, name="otp"),
    path("auth/otp/<int:status>/", otp, name="otp-new"),

    # pages
    path("contact/", contact, name="dashboard-contact"),
    path("change/lang/<lang>/<int:pk>/", change_lan, name="change_lang"),

    # screenshot
    path("generator/<int:pk>/", generator_screen, name="screen-page"),

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

    # pt-diag
    path("patient/add/diag/<int:pk>/<int:status>/", patients, name="dashboard-patient-diag-add"),
    path("patient/edit/diag/<int:pk>/<int:status>/<int:diag_id>/", patients, name="dashboard-patient-diag-edit"),

    # diagnoz
    path("diags/", diagnozs, name="dashboard-diags-list"),
    path("diags/<int:pk>/", diagnozs, name="dashboard-diags-detail"),
    path("diags/add/", diagnoz_form, name="dashboard-diags-add"),
    path("diags/edit/<int:pk>/", diagnoz_form, name="dashboard-diags-edit"),
    path("diags/del/<int:pk>/", diagnoz_del, name="dashboard-diags-delete"),


    # suggest
    path("suggest/add/<int:pk>/<int:status>/", diagnozs, name="add-suggest"),
    path("suggest/add/<int:pk>/<int:status>/<int:suggest_id>/", diagnozs, name="add-suggest"),
]


