from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField('customer status', default=False)
    is_employee = models.BooleanField('employee status', default=False)
