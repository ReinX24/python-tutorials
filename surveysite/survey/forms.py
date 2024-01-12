from django import forms

from survey.models import Row1, Row2


class RowOneForm(forms.ModelForm):
    """Form for showing questions."""

    class Meta:
        model = Row1
        fields = ("question1_1", "question1_2")
        labels = {
            "question1_1": "",
            "question1_2": "",
        }


class RowTwoForm(forms.ModelForm):
    """Second row of questions"""

    class Meta:
        model = Row2
        fields = ("question2_1", "question2_2")
        labels = {
            "question2_1": "",
            "question2_2": "",
        }
