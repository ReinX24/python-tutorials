from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Page for showing the all the stored topics in our database."""
    # Getting all the stored Topic records and sorting them by date_added
    topics = Topic.objects.order_by('date_added')
    # Storing our data in a key value pair.
    context = {'topics': topics}
    # Passing our data to our webpage.
    return render(request, 'learning_logs/topics.html', context)
