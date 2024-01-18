from django.shortcuts import render

from app_owlwatch.forms import QuestionsForm
from app_owlwatch.models import Averages, Questions


# Create your views here.
def index(request):
    """Load index page."""
    # Get the id of the user, QuestionsForm, and Averages
    return render(request, "app_owlwatch/index.html")


def apps_page(request):
    """Load apps page."""
    user_id = request.user.id
    return render(request, "app_owlwatch/apps_page.html", {"user_id": user_id})


def test_page(request, user_id):
    """Load survey page."""

    questions_record = Questions.objects.get(owner_id=user_id)

    if request.method != "POST":
        form = QuestionsForm(instance=questions_record)
    else:
        form = QuestionsForm(instance=questions_record, data=request.POST)
        intensity_1 = request.POST["question1_intensity"]
        frequency_1 = request.POST["question1_frequency"]

        intensity_2 = request.POST["question2_intensity"]
        frequency_2 = request.POST["question2_frequency"]

        intensity_3 = request.POST["question3_intensity"]
        frequency_3 = request.POST["question3_frequency"]

        intensity_4 = request.POST["question4_intensity"]
        frequency_4 = request.POST["question4_frequency"]

        intensity_5 = request.POST["question5_intensity"]
        frequency_5 = request.POST["question5_frequency"]

        # print(intensity_1)
        # print(frequency_1)
        # print(intensity_2)
        # print(frequency_2)
        # print(intensity_3)
        # print(frequency_3)
        # print(intensity_4)
        # print(frequency_4)
        # print(intensity_5)
        # print(frequency_5)

        # form.average_intensity = (float(intensity_1) + float(intensity_2)) / 2
        # form.average_frequency = (float(frequency_1) + float(frequency_2)) / 2

        user_averages = Averages.objects.get(owner_id=user_id)
        user_averages.average_frequency = (float(intensity_1) + float(intensity_2)) / 2
        user_averages.average_intensity = (float(frequency_1) + float(frequency_2)) / 2

        if form.is_valid():
            user_record = form.save(commit=False)
            user_record.owner = request.user
            user_averages.owner = request.user
            user_record.save()
            user_averages.save()

    return render(request, "app_owlwatch/test.html", {"form": form, "user_id": user_id})


def test_history(request, user_id):
    """Get the past tests of the current user."""
    averages = Averages.objects.filter(owner=request.user).order_by("id")
    return render(
        request, "app_owlwatch/test_history.html", {"averages": user_questions}
    )
