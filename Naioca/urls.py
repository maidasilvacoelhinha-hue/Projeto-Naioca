from django.urls import path
from . import views

app_name = "Naioca"

urlpatterns = [
    path("telainicial/", views.telainicial, name="telainicial"),
    path("login/", views.login, name="login"),
    path("sobre/", views.sobre, name="sobre"),
]