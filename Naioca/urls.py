from django.urls import path
from . import views

app_name = "Naioca"

urlpatterns = [
    path("telainicial/", views.telainicial, name="telainicial"),
    path("login/", views.login, name="login"),
    path("sobre/", views.sobre, name="sobre"),
    path("cardapio/", views.menu, name="cardapio"),
    path("criarconta/", views.criarconta, name="criarconta"),
    path("pagamento/", views.pagamento, name="pagamento"),
]