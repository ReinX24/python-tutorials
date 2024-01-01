from django.db import models


# Create your models here.
class Blog(models.Model):
    """A blog that contains the user's name and date created."""

    text = models.CharField(max_length=64)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of our Blog model."""
        return self.text


class Post(models.Model):
    """Posts that each blog contains."""

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Use 'posts' when referring to more than one post."""

        verbose_name_plural = "posts"

    def __str__(self):
        """Return a string representation of our Post model."""
        if len(self.title) <= 50:
            return self.title
        return f"{self.title[:50]}..."
