from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Creating a form from the models we have in our models module."""

    class Meta:
        """
        Tells Django which model the form should be based on and which fields
        to include in the form.
        """

        model = Topic  # form should be based on the Topic model
        fields = ["text"]  # create a textfield
        labels = {"text": ""}  # tells django to not generate a label


class EntryForm(forms.ModelForm):
    """Form for our adding entries related to topics in our database."""

    class Meta:
        """Models and textfields for our entry form."""

        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
