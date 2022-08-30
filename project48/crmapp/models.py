from django.db import models


# Create your models here.

class Lead(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    phoneNumber = models.CharField(unique=True, max_length=15, blank=True)
    secondPhoneNumber = models.CharField(max_length=15, blank=True)
    mail = models.EmailField(max_length=254, blank=True)
    VK = models.CharField(max_length=40, blank=True)
    TG = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

class Status(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=40)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)

    def __str__(self):
        return self.name

class NextAction(models.Model):
    lead = models.ForeignKey(Lead, blank=False, on_delete=models.CASCADE)
    action_type = models.ForeignKey(Action, blank=False, on_delete=models.PROTECT)
    action_date = models.DateField(blank=False)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.lead} - {self.action_type} {self.action_date}'
