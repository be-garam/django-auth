from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    A model to store additional information about a user.

    The default django user model has the following fields:
    - username
    - password
    - email
    - first_name
    - last_name
    - is_active
    - is_staff
    - is_superuser
    - last_login
    - date_joined
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)