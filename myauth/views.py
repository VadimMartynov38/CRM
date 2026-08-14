from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

class MyLoginView(LoginView):
    template_name = "myauth/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("statistic:statistics_dashboard")

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html"
    success_url = reverse_lazy("statistic:statistics_dashboard")

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        authenticated_user = authenticate(
            username=user.username,
            password=form.cleaned_data["password1"],
        )
        if authenticated_user is not None:
            login(self.request, authenticated_user)

        return response


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('myauth:login')