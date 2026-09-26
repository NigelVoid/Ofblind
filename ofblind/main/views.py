from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render

class HomeView(TemplateView):
    template_name = 'main/home.html'

class WhoIsIt_register(View):
    def get(self, request):
        return render(request, 'main/who_register.html')

class WhoIsIt_login(View):
    def get(self, request):
        return render(request, 'main/who_login.html')