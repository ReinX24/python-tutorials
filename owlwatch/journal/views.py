from django.shortcuts import render

from journal.models import Entry


# Create your views here.
def entries(request, user_id):
    """Show the user their entries."""
    entries = Entry.objects.order_by("created_date")
    context = {"entries": entries}
    return render(request, "journal/entries.html", context)
