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
    owner = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of our Post model."""
        if len(self.content) <= 50:
            return f"{self.title}: {self.content}"
        return f"{self.title}: {self.content[:50]}..."