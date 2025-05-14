from django.db import models

# Create your models here.
class Menu(models.Model):
    name        = models.CharField(max_length=50)
    url         = models.CharField(max_length=130)
    icon        = models.CharField(max_length=30, null=True)    
    active      = models.BooleanField(default=True)
    is_parent   = models.BooleanField(default=False)
    parent_id   = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    is_staff    = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Contact(models.Model):
    desc    = models.CharField(max_length=50)
    icon    = models.CharField(max_length=50, default='', null=True)
    contact = models.CharField(max_length=130)
    update  = models.DateTimeField(auto_now=True)
    block   = models.IntegerField(default=0)

    def __str__(self):
        return self.desc