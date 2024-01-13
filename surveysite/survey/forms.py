from django import forms

from survey.models import Questions


class QuestionsForm(forms.ModelForm):
    """Form for showing questions."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-select"

    class Meta:
        model = Questions
        fields = ("question1_1", "question1_2", "question2_1", "question2_2")
        labels = {
            "question1_1": "Intensity",
            "question1_2": "Frequency",
            "question2_1": "Intensity",
            "question2_2": "Frequency",
        }
