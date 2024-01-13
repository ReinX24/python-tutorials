from django import forms

from app_owlwatch.models import Questions


class QuestionsForm(forms.ModelForm):
    """Form for showing questions."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-select"

    class Meta:
        model = Questions
        fields = (
            "question1_intensity",
            "question1_frequency",
            "question2_intensity",
            "question2_frequency",
        )
        labels = {
            "question1_intensity": "Intensity",
            "question1_frequency": "Frequency",
            "question2_intensity": "Intensity",
            "question2_frequency": "Frequency",
        }
