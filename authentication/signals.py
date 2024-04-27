from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile

# Define default image path
DEFAULT_IMAGE_PATH = 'profile_pictures/default.jpg'

# Signal handler for user creation
@receiver(post_save, sender=CustomUser)
def user_create_handler(sender, instance, created, **kwargs):
    """
    this handler create user profile when user register
    """
    if created:
        UserProfile.objects.create(user=instance)
