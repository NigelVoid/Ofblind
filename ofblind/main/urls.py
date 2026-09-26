from django.urls import path
from .views import HomeView, WhoIsIt_register, WhoIsIt_login

app_name = 'main'  

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('who/register/', WhoIsIt_register.as_view(), name='who_register'),
    path('who/login/', WhoIsIt_login.as_view(), name='who_login'),
]
