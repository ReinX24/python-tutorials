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
            "question3_intensity",
            "question3_frequency",
            "question4_intensity",
            "question4_frequency",
            "question5_intensity",
            "question5_frequency",
            "question6_intensity",
            "question6_frequency",
            "question7_intensity",
            "question7_frequency",
            "question8_intensity",
            "question8_frequency",
            "question9_intensity",
            "question9_frequency",
            "question10_intensity",
            "question10_frequency",
            "question11_intensity",
            "question11_frequency",
            "question12_intensity",
            "question12_frequency",
            "question13_intensity",
            "question13_frequency",
            "question14_intensity",
            "question14_frequency",
            "question15_intensity",
            "question15_frequency",
            "question16_intensity",
            "question16_frequency",
            "question17_intensity",
            "question17_frequency",
        )
        labels = {
            "question1_intensity": "Intensity",
            "question1_frequency": "Frequency",
            "question2_intensity": "Intensity",
            "question2_frequency": "Frequency",
            "question3_intensity": "Intensity",
            "question3_frequency": "Frequency",
            "question4_intensity": "Intensity",
            "question4_frequency": "Frequency",
            "question5_intensity": "Intensity",
            "question5_frequency": "Frequency",
            "question6_intensity": "Intensity",
            "question6_frequency": "Frequency",
            "question7_intensity": "Intensity",
            "question7_frequency": "Frequency",
            "question8_intensity": "Intensity",
            "question8_frequency": "Frequency",
            "question9_intensity": "Intensity",
            "question9_frequency": "Frequency",
            "question10_intensity": "Intensity",
            "question10_frequency": "Frequency",
            "question11_intensity": "Intensity",
            "question11_frequency": "Frequency",
            "question12_intensity": "Intensity",
            "question12_frequency": "Frequency",
            "question13_intensity": "Intensity",
            "question13_frequency": "Frequency",
            "question14_intensity": "Intensity",
            "question14_frequency": "Frequency",
            "question15_intensity": "Intensity",
            "question15_frequency": "Frequency",
            "question16_intensity": "Intensity",
            "question16_frequency": "Frequency",
            "question17_intensity": "Intensity",
            "question17_frequency": "Frequency",
        }
