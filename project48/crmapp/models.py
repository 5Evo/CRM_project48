'''
this module keeps models for DB
'''
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from userapp.models import CrmUser


# class UserManager(models.Manager):
#     def get_queryset(self):
#         all_objects = super().get_queryset()
#         return all_objects.filter(user=self)


# Протестируем ответ в StackOverflow:
class UserQuerySet(models.QuerySet):
    def get_by_user(self, request):
        return self.filter(user=request.user)


class Tag(models.Model):
    '''
    The Class (model for DB) for Tags
    '''
    objects = models.Manager()
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.name}'


class Lead(models.Model):
    '''
    The Class (model for DB) of Leads
    '''
    #objects = models.Manager()
    #user_objects = UserQuerySet.as_manager()
    objects = UserQuerySet.as_manager()

    first_name = models.CharField(max_length=40, verbose_name='Name')
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, verbose_name='Last name')
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    phoneNumber = PhoneNumberField(null=True, blank=True, verbose_name='Phone')
    mail = models.EmailField(max_length=254, blank=True, verbose_name='Email')
    VK = models.CharField(max_length=40, blank=True)
    TG = models.CharField(max_length=40, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='avatar', null=True, blank=True)
    user = models.ForeignKey(CrmUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    def has_image(self):
        return bool(self.image)


class Status(models.Model):
    '''
    The Class (model for DB) of Statuses of Lead
    '''
    objects = models.Manager()

    name = models.CharField(unique=True, blank=False, max_length=40)

    def __str__(self):
        return str(self.name)


class Action(models.Model):
    '''
    TThe Class (model for DB) of Action's types for Leads
    '''
    objects = models.Manager()

    name = models.CharField(unique=True, blank=False, max_length=30)

    def __str__(self):
        return str(self.name)


class NextAction(models.Model):
    '''
    The Class (model for DB) for Action with Lead
    '''
    objects = models.Manager()

    lead = models.ForeignKey(Lead, blank=False, on_delete=models.CASCADE)
    action_type = models.ForeignKey(Action, blank=False, on_delete=models.PROTECT)
    action_date = models.DateField(blank=False)
    create = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.lead} - {self.action_type} {self.action_date}'
