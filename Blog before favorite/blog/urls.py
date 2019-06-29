from django.urls import path 
from blog.views import home,details

app_name ='blog'
urlpatterns =[
    path('', home),
    path('<int:blog_id>/', details,name ='any_name' ),

]