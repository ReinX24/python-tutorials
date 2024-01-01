from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from blogs.models import Blog, Post
from blogs.forms import BlogForm, PostForm


# Create your views here.
def index(request):
    """Index page for our Blog."""
    return render(request, "blogs/index.html")


@login_required
def blogs_page(request):
    """Return the different types of blogs for our page."""
    # blogs = Blog.objects.order_by("date_added")
    blogs = Blog.objects.filter(owner=request.user).order_by("date_added")
    context = {"blogs": blogs}
    return render(request, "blogs/blogs.html", context)


@login_required
def posts(request, blog_id):
    """Return the different posts for each blog."""
    blog = Blog.objects.get(id=blog_id)

    check_blog_owner(request, blog)

    posts = blog.post_set.order_by("-date_added")
    context = {"blog": blog, "posts": posts}
    return render(request, "blogs/posts.html", context)


@login_required
def new_blog(request):
    """Add a new blog page to our website."""
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect("blogs:blogs_page")

    context = {"form": form}
    return render(request, "blogs/new_blog.html", context)


@login_required
def new_post(request, blog_id):
    """Add a new post to a blog."""
    blog = Blog.objects.get(id=blog_id)

    check_blog_owner(request, blog)

    if request.method != "POST":
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect("blogs:posts", blog_id=blog_id)

    context = {"form": form, "blog": blog}
    return render(request, "blogs/new_post.html", context)


@login_required
def edit_post(request, post_id):
    """Edit an existing post of a blog."""
    # Getting the post object and the blog associated with the post.
    post = Post.objects.get(id=post_id)
    blog = post.blog

    check_blog_owner(request, blog)

    if request.method != "POST":
        # Returns a form with data from the post.
        form = PostForm(instance=post)
    else:
        # Updating the existing post data with new post data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs:posts", blog_id=blog.id)

    # Returns the form with the current data if any request other than a POST
    # request is made.
    context = {"form": form, "blog": blog, "post": post}
    return render(request, "blogs/edit_post.html", context)


def check_blog_owner(request, blog):
    """Check if the current blog's owner is the same with the current user."""
    if blog.owner != request.user:
        raise Http404
