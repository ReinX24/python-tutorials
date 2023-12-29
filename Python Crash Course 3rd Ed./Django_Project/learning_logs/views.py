from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Page for showing the all the stored topics in our database."""
    # Getting all the stored Topic records and sorting them by date_added.
    topics = Topic.objects.order_by('date_added')
    # Storing our data in a key value pair.
    context = {'topics': topics}
    # Passing our data to our webpage.
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Get the entries associated with the topic, most recently added first.
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """
    Show a blank form where the user could enter data, redirects back to topics
    page after submitting the form.
    """
    if request.method != 'POST':
        # No data submitted; create a blank form.
        # This runs when the page is initially loaded or a GET request is made.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        # The data that the user has in the form will be in request.POST.
        form = TopicForm(data=request.POST)
        # Checking if all required fields are filled in.
        if form.is_valid():
            # Writing data from our form to our database.
            form.save()
            # Redirects the user back to the topics page.
            return redirect('learning_logs:topics')
        
    # Display a blank or invalid form, returns when any request other than 
    # a POST request is made.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; create a blank form.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)