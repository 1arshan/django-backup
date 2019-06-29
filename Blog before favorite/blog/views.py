from django.http import Http404
from blog.models import Blogs
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    all_blog = Blogs.objects.all()
    #return HttpResponse("Hello,welcome to bLOGGER")    
    return render(request,'blog/home.html',{
        'all_blogs' : all_blog
    })

def details(request, blog_id):
    try:
        all_blog1 = Blogs.objects.get(pk =blog_id)
    except Blogs.Does.Not.Exit:
        raise Http404("Blogs does not exist")    
    return render(request,'blog/details.html',{
         'all_blog1' :all_blog1  
        #'all_blog1' : Blogs.objects.filter(id =blog_id)
    })

# Create your views here.
    