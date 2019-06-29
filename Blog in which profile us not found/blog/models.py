from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Blogs(models.Model):

    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    author = models.OneToOneField(User,to_field='username',on_delete =models.CASCADE)
    #author = models.ForeignKey(User,unique=True,to_field='username',on_delete =models.CASCADE)  
    #author = models.CharField(max_length =50,unique =True)
    blog_logo = models.FileField(blank =True)
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Blogs.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        #instance.profile.save()
        instance.username.save()
    
    
    def get_absolute_url(self):
        return reverse ('blog:any_name', kwargs ={'pk':self.pk})
    #def __str__(self):
        #return self.author.username
    
class Blogs1(models.Model):
    Author =models.ForeignKey(Blogs,on_delete =models.CASCADE)
    blog_content = models.CharField(max_length =250)
    is_favorite =models.BooleanField(default =False)
    def __str__(self):
        return self.blog_content
