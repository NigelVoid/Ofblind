from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Электронная почта")

    status = forms.ChoiceField(
        choices=User.USER_STATUS_CHOICES,
        required=True, 
        label="Статус профиля"
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'status')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) > 11:
            raise ValidationError("Имя пользователя не может быть длиннее 11 символов.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с такой почтой уже зарегистрирован.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        if commit:
            user.save()
        return user