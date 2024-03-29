from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Blogs(models.Model):

    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.OneToOneField(User,to_field='username',on_delete =models.CASCADE)
    #author = models.ForeignKey(User,unique=True,to_field='username',on_delete =models.CASCADE)  
    #author = models.CharField(max_length =50,unique =True)
    blog_logo = models.FileField()
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse ('blog:any_name', kwargs ={'pk':self.pk})
    def __str__(self):
        return self.author.username
 
class Blogs1(models.Model):
    Author =models.ForeignKey(Blogs,on_delete =models.CASCADE)
    blog_content = models.CharField(max_length =250)
    is_favorite =models.BooleanField(default =False)
    def __str__(self):
        return self.blog_content
