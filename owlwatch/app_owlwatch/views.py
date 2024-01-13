from django.shortcuts import render

from app_owlwatch.forms import QuestionsForm


# Create your views here.
def index(request):
    """Load index page."""
    return render(request, "app_owlwatch/index.html")


def test_page(request):
    """Load survey page."""
    if request.method == "POST":
        form = QuestionsForm(data=request.POST)
        intensity_1 = request.POST["question1_intensity"]
        frequency_1 = request.POST["question1_frequency"]
        intensity_2 = request.POST["question2_intensity"]
        frequency_2 = request.POST["question2_frequency"]
        print(intensity_1)
        print(frequency_1)
        print(intensity_2)
        print(frequency_2)
    else:
        form = QuestionsForm()

    return render(request, "app_owlwatch/test.html", {"form": form})
