from django.views.generic import FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import RegisterForm

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)