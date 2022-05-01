import imp
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name="navigation"

urlpatterns = [
    path("", views.index, name="index")
]
