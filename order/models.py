from django.db import models
from django.urls import reverse

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=5)
    order = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order:order_detail', kwargs={'pk':self.pk})
