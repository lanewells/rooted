from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import RelativeProfile

@receiver(post_save, sender=User)
def create_relative_profile(sender, instance, created, **kwargs):
    if created: 
        RelativeProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_relative_profile(sender, instance, **kwargs):
    if hasattr(instance, 'relativeprofile'):
        instance.relativeprofile.save()