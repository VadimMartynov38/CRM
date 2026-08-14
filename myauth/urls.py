from django.urls import path

from .views import (
    MyLogoutView,
    RegisterView,
    MyLoginView,
)

app_name = "myauth"

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),

]
