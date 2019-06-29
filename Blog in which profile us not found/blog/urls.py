from django.urls import path 
from blog import views

app_name ='blog'
urlpatterns =[
    path('', views.homeview.as_view(),name ='home'),
    path('<int:pk>/', views.detailview.as_view(),name ='any_name'),
    path('blogs/',views.blogcreate.as_view(),name ='blog_add'),
    path('blogs1/add/<int:pk>/',views.blog1create.as_view(),name ='blog_content_add'),
    #update_blog
    path('blogs/<int:pk>/',views.blogupdate.as_view(),name ='blog_update'),
    #delete
    path('blogs/<int:pk>/delete/',views.blogdelete.as_view(),name ='blog_delete'), 

    #registration
    path('register/',views.UserFormview.as_view(),name ='register'),
    path('search/',views.search,name ='search'),




    
]