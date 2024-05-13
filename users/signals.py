from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile

User = get_user_model()

"""
The @receiver decorator is used to attaching functions or methods to
the signals
"""

@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    """
    This is a signal handler which cretes a corressponding Profile
    instance when the user is created
    """
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    """
    This is a signal handler which saves corressponding Profile instance
    associated with the user.
    """
    instance.profile.save()

