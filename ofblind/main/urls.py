from django.urls import path
from .views import HomeView, WhoIsIt_register, WhoIsIt_login

app_name = 'main'  

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]
