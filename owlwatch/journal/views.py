from django.shortcuts import redirect, render
from journal.forms import EntryForm

from journal.models import Entry


# Create your views here.
def entries(request, user_id):
    """Show the user their entries."""
    entries = Entry.objects.filter(owner=user_id).order_by("created_date")
    context = {"entries": entries, "user_id": user_id}
    return render(request, "journal/entries.html", context)


def add_entry(request, user_id):
    """Add an entry for our user."""
    if request.method == "POST":
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return redirect("journal:entries", user_id=user_id)
    else:
        form = EntryForm()

    return render(request, "journal/add_entry.html", {"form": form, "user_id": user_id})


def entry_info(request, entry_id):
    """Show the full text of the Entry."""
    entry = Entry.objects.get(id=entry_id)
    user_id = request.user.id
    return render(
        request, "journal/entry_info.html", {"entry": entry, "user_id": user_id}
    )


def edit_entry(request, entry_id):
    """Edit an existing Entry of the user."""
    return render(request, "journal/edit_entry.html")
