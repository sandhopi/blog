from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ContentBlog(models.Model):

    author      = models.CharField(max_length=50)
    title       = models.CharField(max_length=255)
    image       = models.ImageField(blank=True)    
    content     = RichTextUploadingField()
    category    = models.ForeignKey(Category, default=None, on_delete=models.CASCADE)
    active      = models.BooleanField(default=False)
    created     = models.DateTimeField(auto_now=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Subscriber(models.Model):
    email       = models.CharField(max_length=100)
    created     = models.DateTimeField(auto_now=True)
    updated     = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.email
    
class UrlPerfom(models.Model):
    url             = models.CharField(max_length=200)
    click_element   = models.CharField(max_length=200)
    scroll_position = models.CharField(max_length=20)
    used_time       = models.CharField(max_length=200)
    user_agent      = models.CharField(max_length=200)
    see_user_id     = models.CharField(max_length=200)
    created         = models.DateTimeField(auto_now=True)
    updated         = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.url

    