from django.shortcuts import render

from survey.forms import QuestionsForm


# Create your views here.
def test_page(request):
    """Load survey page."""
    if request.method == "POST":
        form = QuestionsForm(data=request.POST)
        intensity_1 = request.POST["question1_1"]
        frequency_1 = request.POST["question1_2"]
        intensity_2 = request.POST["question2_1"]
        frequency_2 = request.POST["question2_2"]
        print(intensity_1)
        print(frequency_1)
        print(intensity_2)
        print(frequency_2)
    else:
        form = QuestionsForm()

    return render(request, "owl_watch/test.html", {"form": form})
