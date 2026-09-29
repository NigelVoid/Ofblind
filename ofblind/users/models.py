# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import parse_github_skills

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

class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='applicant_profile')
    skills = models.TextField(blank=True,
                              verbose_name="Навыки")
    github_username = models.CharField(max_length=100,
                                       blank=True,
                                       verbose_name="GitHub")
    resume = models.FileField(upload_to='resumes/',
                              blank=True,
                              null=True,
                              verbose_name="Файл резюме")

    def __str__(self):
        return f"Резюме соискателя: {self.user.username}"

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='employer_profile')
    company_name = models.CharField(max_length=255,
                                    blank=True,
                                    verbose_name="Название компании")
    website = models.URLField(blank=True,
                              verbose_name="Сайт компании")

    def __str__(self):
        return f"Компания: {self.company_name} ({self.user.username})"


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.status == 'applicant':
            profile = ApplicantProfile.objects.create(user=instance)
            if profile.github_username:
                profile.skills = parse_github_skills(profile.github_username)

            profile.save()
            
        elif instance.status == 'employer':
            EmployerProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.status == 'applicant' and hasattr(instance, 'applicant_profile'):
        instance.applicant_profile.save()
    elif instance.status == 'employer' and hasattr(instance, 'employer_profile'):
        instance.employer_profile.save()