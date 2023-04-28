from django.urls import path

from .views import omlet, pasta

urlpatterns = [
    path("omlet/", omlet, name="omlet"),
    path("pasta/", pasta, name="pasta"),
]