import os

from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ 
from django.db import models
from users.managers import CustomUserManager

def get_image_filename(instance, filename):
    """
    This function is responsible for generating unique filename 
    to each of the uploaded image
    """
    name = instance.user.username
    slug = slugify(name)
    """
    slugify function is a utility provided by django which converts string
    into a slug which is a url friendly version of the string. It replaces
    characters with hyphens and converts the string to lowercase ensuring 
    filename is url is safe and standardized
    """
    return f"products/{slug}-{filename}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_image_filename, blank=True)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.user.email 
    
    @property
    def filename(self):
        """
        It extracts the filename stored from the full path of the 
        avatar image stored in the database
        """
        return os.path.basename(self.avatar.name)
    

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique = True )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email


