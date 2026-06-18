from django.urls import path
from . import views

app_name = "nome_do_app"

urlpatterns = [
    path("", views.telainicial, name="telainicial"),
    path("paginadelogin/", views.paginadelogin, name="paginadelogin"),
    path("sobre/", views.sobre, name="sobre"),
]