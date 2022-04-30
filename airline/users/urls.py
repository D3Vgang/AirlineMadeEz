from telnetlib import LOGOUT
from django.urls import path

from . import views

urlpatterns = [
    path("", views.userindex, name="userindex"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]
