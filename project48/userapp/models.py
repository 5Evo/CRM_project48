from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CrmUser(AbstractUser):
    # email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True)
