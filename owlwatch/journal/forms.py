from django import forms

from journal.models import Entry


class EntryForm(forms.ModelForm):
    """Form for adding journal entries."""

    class Meta:
        model = Entry
        fields = ("title", "text")
        labels = {"title": "Title", "text": "Entry"}
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": ""}),
            "text": forms.Textarea(attrs={"placeholder": ""}),
        }
