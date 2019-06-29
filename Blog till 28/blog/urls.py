from django.urls import path 
from blog.views import home,details,favorite

app_name ='blog'
urlpatterns =[
    path('', home),
    path('<int:blog_id>/', details,name ='any_name' ),
    path('<int:blog_id>/favorite/',favorite,name ='favorite'),

]