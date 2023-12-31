from django.urls import path

from . import views


app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Blogs page
    path('blogs/', views.blogs_page, name='blogs_page'),
    # Posts for each blog page
    path('posts/<int:blog_id>/', views.posts, name='posts'),
    # Add a new blog page to our blogs
    path('new_blog/', views.new_blog, name='new_blog'),
    # Add a new post to one of our blogs
    path('new_post/<int:blog_id>', views.new_post, name='new_post'),
]