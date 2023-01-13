from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):

    name = models.CharField(max_length=50,)
    company_name = models.CharField(max_length=50, default='')

    email = models.EmailField(max_length=254, unique=True)

    username = None

    USERNAME_FIELD = 'email'

    phone = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # my modifications 
    # zoho 
    access_token = models.CharField(max_length=250, blank=True, null=True,default='default12334')
    refresh_token = models.CharField(max_length=250, blank=True, null=True,default='')
    client_id = models.CharField(max_length=250, blank=True, null=True, default='')
    client_secret = models.CharField(max_length=250, blank=True, null=True, default='')
    zoho_domain = models.CharField(max_length=250, blank=True, null=True, default='')

    # cloudfare 
    cloudfare_email = models.CharField(max_length=250, blank=True, null=True, default='')
    cloudfare_auth_code = models.CharField(max_length=250, blank=True, null=True, default='')
    
    # smart lead

    smart_lead_api_key =  models.CharField(max_length=250, blank=True, null=True,default='')
     
    # api calls 

    api_calls = models.IntegerField(blank=True, default=0, null=True)
    
    # celery 

    celery_task_id_add_domain_list = models.TextField(max_length=25000, blank=True, null=True, default='')
    celery_task_id_create_user_zoho_list = models.TextField(max_length=25000, blank=True, null=True, default='')
    celery_task_id_create_user_zoho_smartlead_list = models.TextField(max_length=25000, blank=True, null=True, default='')

    # verify user to login 

    access_allowed = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['name']
