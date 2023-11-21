from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
import datetime
from django.utils.text import slugify

# Create your models here.
'''
   1- html widget
   2- validation
   3- best for database
'''
# create database               
class Post(models.Model):
    title=models.CharField(max_length=100,verbose_name=_('Name_Post'))
    content=models.TextField(max_length=1000,verbose_name=_('Content_Post'))
    draft=models.BooleanField(default=True,verbose_name=_('Active'))
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author',verbose_name=_('Name_Author'))
    tags = TaggableManager()
    image=models.ImageField(upload_to='photo',verbose_name=_('image'))
    slug=models.SlugField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,related_name='post_category')

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Comments(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comment_author')
    content=models.TextField(max_length=350)
    image=models.ImageField(upload_to='photo_comment')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment_post')
    publish_date=models.DateTimeField(default=datetime.datetime.now)
     
    def __str__(self):
        return str(self.post)

