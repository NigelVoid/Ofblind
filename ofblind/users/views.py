from django.contrib.auth import logout, get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import FormView, DetailView
from django.views import View
from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.conf import settings

User = get_user_model()

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        user = form.save()
        
        current_site = get_current_site(self.request)
        subject = 'Активация вашего аккаунта'
        
        message = render_to_string('users/activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        
        send_mail(
            subject=subject, 
            message=message, 
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(View):
    def get(self, request):
        logout(request)

        return redirect('main:home')


def activate_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/activation_success.html')
    else:
        return render(request, 'users/activation_invalid.html')

def register_done_view(request):
    return render(request, 'users/register_done.html')

class ProfileDetailView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'profile_user' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_obj = self.get_object()
        
        if user_obj.status == 'applicant' and hasattr(user_obj, 'applicant_profile'):
            skills_str = user_obj.applicant_profile.skills
            if skills_str:
                context['skills_list'] = [s.strip() for s in skills_str.split(',') if s.strip()]
        return context
