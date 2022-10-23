from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CrmUser(AbstractUser):
    # email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True, blank=True)
    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'
    def has_avater(self):
        return bool(self.avatar)

    # В данный момент у каждого пользователя собственные лиды. функционал доступа нескольких пользователей
    # к одной базе лидов не реализован
    # is_admin = models.BooleanField()
