from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Email as a unique identifier
    profile_picture = models.ImageField(upload_to='user_profiles/', blank=True, null=True)  # Profile picture
    location = models.CharField(max_length=255, blank=True, null=True)  # User location
    phone=models.CharField(max_length=10,blank=True,null=True)
    is_admin = models.BooleanField(default=False) 
    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']


class Author(models.Model):
    first_name = models.CharField(max_length=100)  # Author's first name
    last_name = models.CharField(max_length=100)   # Author's last name
    bio = models.TextField(blank=True, null=True)  # Short biography
    date_of_birth = models.DateField(blank=True, null=True)  # Date of birth
    date_of_death = models.DateField(blank=True, null=True)  # Date of death (optional)
    website = models.URLField(blank=True, null=True)  # Author's website
    photo = models.ImageField(upload_to='author_photos/', blank=True, null=True)  # Author's photo

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']  # Order by last and first name