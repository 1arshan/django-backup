from django.http import Http404
from blog.models import Blogs,Blogs1
from django.shortcuts import render,get_object_or_404
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
        blog_id1 =blog_id
    except Blogs.Does.Not.Exit:
        raise Http404("Blogs does not exist")    
    return render(request,'blog/details.html',{
         'all_blog1' :all_blog1 ,'blog_id1' :blog_id1 
        #'all_blog1' : Blogs.objects.filter(id =blog_id)
    })


def favorite(request,blog_id):
    all_blog1 =get_object_or_404(Blogs, pk =blog_id)
    blog_id1 =blog_id
    try:

        selected_blog =all_blog1.blogs1_set.get(pk =request.POST['x'])
    except(KeyError):
    #except(KeyError,blog1.Does.Not.Exist):
        return render(request,'blog/details.html',{
            'all_blog1': all_blog1 ,'blog_id1' :blog_id1,'error_message' : "you did not select a valid blog"
        })
    else: 
        selected_blog.is_favorite =True
        selected_blog.save()
    return render(request,'blog/details.html',{
        'all_blog1': all_blog1 ,'blog_id1' :blog_id1
            })


# Create your views here.
    