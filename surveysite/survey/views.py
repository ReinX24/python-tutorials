from django.shortcuts import render

from survey.forms import RowOneForm, RowTwoForm


# Create your views here.
def survey_page(request):
    """Load survey page."""
    if request.method == "POST":
        form1 = RowOneForm(data=request.POST)
        form2 = RowTwoForm(data=request.POST)
    else:
        form1 = RowOneForm()
        form2 = RowTwoForm()

    return render(request, "survey/survey.html", {"form1": form1, "form2": form2})
