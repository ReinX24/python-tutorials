from django.shortcuts import render

from app_owlwatch.forms import QuestionsForm
from app_owlwatch.models import Averages


# Create your views here.
def index(request):
    """Load index page."""
    return render(request, "app_owlwatch/index.html")


def apps_page(request):
    """Load apps page."""
    return render(request, "app_owlwatch/apps_page.html")


def test_page(request):
    """Load survey page."""
    if request.method == "POST":
        form = QuestionsForm(data=request.POST)
        intensity_1 = request.POST["question1_intensity"]
        frequency_1 = request.POST["question1_frequency"]
        intensity_2 = request.POST["question2_intensity"]
        frequency_2 = request.POST["question2_frequency"]

        # print(intensity_1)
        # print(frequency_1)
        # print(intensity_2)
        # print(frequency_2)

        # form.average_intensity = (float(intensity_1) + float(intensity_2)) / 2
        # form.average_frequency = (float(frequency_1) + float(frequency_2)) / 2

        # When the user makes a new account, creat an instance of QuestionsForm
        # and Averages already, this is so that there will only be one instance
        # instead of several instances of their averages and test answers.
        user_averages = Averages()
        user_averages.average_frequency = 5
        user_averages.average_intensity = 10

        if form.is_valid():
            user_record = form.save(commit=False)
            user_record.owner = request.user
            user_averages.owner = request.user
            user_record.save()
            user_averages.save()
    else:
        form = QuestionsForm()

    return render(request, "app_owlwatch/test.html", {"form": form})
