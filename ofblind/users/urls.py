from django.urls import path
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, 
                                       PasswordResetConfirmView, PasswordResetCompleteView)
from .views import RegisterView, LoginView, LogoutView, register_done_view, activate_view, ProfileDetailView

app_name = 'users'  

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/done/', register_done_view, name='register_done'),
    path('activate/<uidb64>/<token>/', activate_view, name='activate'),
    path('password-reset/', PasswordResetView.as_view(
             template_name='users/password_reset_form.html',
             email_template_name='users/password_reset_email.html', # шаблон письма
             success_url='/users/password-reset/done/'
         ), 
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html',
             success_url='/users/password-reset/complete/'
         ), 
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
]
