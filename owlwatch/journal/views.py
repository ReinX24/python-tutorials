from django.shortcuts import redirect, render
from journal.forms import EntryForm
from journal.models import Entry
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def entries(request, user_id):
    """Show the user their entries."""
    entries = Entry.objects.filter(owner=user_id).order_by("created_date")
    context = {"entries": entries, "user_id": user_id}
    return render(request, "journal/entries.html", context)


@login_required
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


@login_required
def entry_info(request, entry_id):
    """Show the full text of the Entry."""
    entry = Entry.objects.get(id=entry_id)
    user_id = request.user.id
    return render(
        request, "journal/entry_info.html", {"entry": entry, "user_id": user_id}
    )


@login_required
def edit_entry(request, entry_id):
    """Edit an existing Entry of the user."""
    entry = Entry.objects.get(id=entry_id)

    if request.method == "POST":
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.owner = request.user
            entry.save()
            return redirect("journal:entry_info", entry_id=entry_id)
    else:
        form = EntryForm(instance=entry)

    return render(request, "journal/edit_entry.html", {"form": form, "entry": entry})


@login_required
def delete_entry(request, entry_id):
    """Delete an existing Entry of the user."""
    entry = Entry.objects.get(id=entry_id)
    if request.method == "POST":
        entry.delete()
        return redirect("journal:entries", user_id=request.user.id)

    return render(request, "journal/delete_entry.html", {"entry": entry})
