from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def save_relative_profile(sender, instance, **kwargs):
    if hasattr(instance, 'relativeprofile'):
        instance.relativeprofile.save()