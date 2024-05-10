from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='all_posts'),
    path('posts/<str:slug>', views.post_detail, name='detail')
    

]
