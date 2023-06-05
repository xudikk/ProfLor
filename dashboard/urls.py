from django.urls import path

from dashboard.services.auth import sign_in, sign_out, otp
from .services.auto import auto_form, gets
from .services.contact import contact

from .views import index

urlpatterns = [
    # auth
    path("", index, name="dash_home"),
    path("auth/", sign_in, name="sign-in"),
    path("auth/logout/", sign_out, name="sign-out"),
    path("auth/logout/<conf>/", sign_out, name="sign-out-conf"),

    # auth-otp
    path("auth/otp/", otp, name="otp"),
    path("auth/otp/<int:status>/", otp, name="otp-new"),

    # # pages
    path("contact/", contact, name="dashboard-contact"),

    # auto
    path("<key>/", gets, name="dashboard-auto-list"),
    path("<key>/<int:pk>/", gets, name="dashboard-auto-detail"),
    path("<key>/add/", auto_form, name="dashboard-auto-add"),
    path("<key>/edit/<int:pk>/", auto_form, name="dashboard-auto-edit"),

]
