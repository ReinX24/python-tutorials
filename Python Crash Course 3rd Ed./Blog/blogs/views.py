from django.shortcuts import render, redirect
from blogs.forms import BlogForm, PostForm

from blogs.models import Blog


# Create your views here.
def index(request):
    """Index page for our Blog."""
    return render(request, 'blogs/index.html')


def blogs_page(request):
    """Return the different types of blogs for our page."""
    blogs = Blog.objects.order_by('date_added')
    context = {"blogs": blogs}
    return render(request, 'blogs/blogs.html', context)


def posts(request, blog_id):
    """Return the different posts for each blog."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.order_by('-date_added')
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/posts.html', context)


def new_blog(request):
    """Add a new blog page to our website."""
    if request.method != 'POST':
        form = BlogForm()
    else: 
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs_page')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)


def new_post(request, blog_id):
    """Add a new post to a blog."""
    blog = Blog.objects.get(id=blog_id)
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:posts', blog_id=blog_id)
        
    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_post.html', context)

# TODO: add a feature where we could edit a post from a blog