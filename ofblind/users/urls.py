from django.urls import path
from .views import RegisterView, LoginView, LogoutView, register_done_view, activate_view

app_name = 'users'  

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/done/', register_done_view, name='register_done'),
    path('activate/<uidb64>/<token>/', activate_view, name='activate'),
]
