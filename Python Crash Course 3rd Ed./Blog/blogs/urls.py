from django.urls import path

from . import views


app_name = "blogs"
urlpatterns = [
    # Home page
    path("", views.index, name="index"),
    # Blogs page
    path("blogs/", views.blogs_page, name="blogs_page"),
    # Posts for each blog page
    path("posts/<int:blog_id>/", views.posts, name="posts"),
    # Add a new blog page to our blogs
    path("new_blog/", views.new_blog, name="new_blog"),
    # Add a new post to one of our blogs
    path("new_post/<int:blog_id>", views.new_post, name="new_post"),
    # Edit a post in one of our blogs.
    path("edit_post/<int:post_id>", views.edit_post, name="edit_post"),
    # Delete a blog and its posts
    path("delete_blog/<int:blog_id>", views.delete_blog, name="delete_blog"),
    # Delete a post from a blog
    path("delete_post/<int:post_id>", views.delete_post, name="delete_post"),
]
