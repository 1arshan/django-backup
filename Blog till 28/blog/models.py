from django.db import models

class Blogs(models.Model):
    author = models.CharField(max_length =50)
    
    created_at = models.DateTimeField(auto_now=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.author
 
class Blogs1(models.Model):
    Author =models.ForeignKey(Blogs,on_delete =models.CASCADE)
    blog_content = models.CharField(max_length =250)
    is_favorite =models.BooleanField(default =False)
    def __str__(self):
        return self.blog_content
