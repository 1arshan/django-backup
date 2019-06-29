from django.http import Http404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from blog.models import Blogs,Blogs1
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.views.generic import View
from .forms import UserForm
from django.db.models import Q
from rest_framework import viewsets
from blog.serializers import bloggerserializer

class homeview(generic.ListView):
    template_name ='blog/home.html'
    context_object_name ='all_blogs'

    def get_queryset(self):
        return Blogs.objects.all()

class detailview(generic.DetailView):
    model =Blogs
    template_name ='blog/details.html'



class blogcreate(CreateView):
    model =Blogs
    fields =['author','blog_logo']
    template_name ='blog/blogs.html'

class blog1create(CreateView):
    model =Blogs1
    fields =['Author','blog_content']
    template_name ='blog/blogs1.html'
    def get_success_url(self):
        return reverse('blog:home')


class blogupdate(UpdateView):
    model =Blogs
    field =['author','blog_logo']

class blogdelete(DeleteView):
    model =Blogs
    success_url =reverse_lazy( 'blog:home')        
    

    
class UserFormview(View):
    form_class =UserForm
    template_name ='blog/registration_form.html'

    #display blank form
    def get(self,request):
        form =self.form_class(None)
        return render (request,self.template_name,{'form' :form})
    #display full fill form    
    def post(self,request):
        form =self.form_class(request.POST)
        if form.is_valid():
            user =form.save(commit =False)
            #cleaned (normalized ) data
            username =form.cleaned_data['username']
            password =form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user onjects if credential are correct
            user = authenticate(username =username, password =password)

            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return redirect('blog:home')
        return render(request,self.template_name ,{'form':form})            

def search(request):
    if request.method =="GET":
        query =request.GET.get('q')

        submitbutton =request.GET.get("submit")

        if query is not None:
            lookups =Q(blog_content__icontains=query)

            results=Blogs1.objects.filter(lookups).distinct()

            return render(request,'blog/base.html',{'results':results,'submitbutton':submitbutton})
        else:
            return render (request,'blog/base.html')   
    else:
        return render(request,'blog/base.html')     

class bloggerViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class =bloggerserializer