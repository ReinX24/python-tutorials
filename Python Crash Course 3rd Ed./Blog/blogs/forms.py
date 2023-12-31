from django import forms

from blogs.models import Blog, Post


class BlogForm(forms.ModelForm):
    """Creating a form for creating a new blog page."""
    class Meta:
        """Chooses which model will be used for our form."""
        model = Blog
        fields = ['text']
        labels = {'text': ''} # no label for our text field


class PostForm(forms.ModelForm):
    """Creating a form for creating a new post for a blog."""
    class Meta:
        """Sets which model we will be making a form for."""
        model = Post
        fields = ['title', 'content']
        labels = {'title': 'Title', 'content': 'Content'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}