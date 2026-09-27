# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_STATUS_CHOICES = [
        ('applicant', 'Соискатель'),
        ('employer', 'РАБотодатель'),
    ]

    status = models.CharField(choices=USER_STATUS_CHOICES, 
                              null=True, 
                              verbose_name='Статус профиля')

    def __str__(self):
        return self.username
