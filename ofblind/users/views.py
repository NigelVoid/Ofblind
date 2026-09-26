from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import RegisterForm

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('main:home')