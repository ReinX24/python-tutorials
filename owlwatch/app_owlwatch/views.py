from django.shortcuts import render

from app_owlwatch.forms import QuestionsForm
from app_owlwatch.models import Averages, Questions
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """Load index page."""
    # Get the id of the user, QuestionsForm, and Averages
    return render(request, "app_owlwatch/index.html")


@login_required
def apps_page(request):
    """Load apps page."""
    user_id = request.user.id
    return render(request, "app_owlwatch/apps_page.html", {"user_id": user_id})


@login_required
def test_page(request, user_id):
    """Load survey page."""

    questions_record = Questions.objects.get(owner_id=user_id)

    if request.method != "POST":
        form = QuestionsForm(instance=questions_record)
    else:
        form = QuestionsForm(instance=questions_record, data=request.POST)

        intensity_total = 0
        frequency_total = 0
        for i in range(1, 18):
            intensity_total += int(request.POST[f"question{i}_intensity"])
            frequency_total += int(request.POST[f"question{i}_frequency"])

        print(intensity_total)
        print(frequency_total)

        user_averages = Averages.objects.get(owner_id=user_id)
        user_averages.average_intensity = intensity_total / 17
        user_averages.average_frequency = frequency_total / 17

        if form.is_valid():
            user_record = form.save(commit=False)
            user_record.owner = request.user
            user_averages.owner = request.user
            user_record.save()
            user_averages.save()

            context = {
                "average_intensity": float(user_averages.average_intensity),
                "average_frequency": float(user_averages.average_frequency),
                "user_id": user_id,
            }

            return render(request, "app_owlwatch/results.html", context)

    return render(request, "app_owlwatch/test.html", {"form": form, "user_id": user_id})


@login_required
def test_reset(request, user_id):
    """Reset the values in our test_page."""
    questions_record = Questions.objects.get(owner_id=user_id)

    if request.method != "POST":
        # Reset all the values of test_reset
        questions_record.question1_intensity = 0
        questions_record.question2_intensity = 0
        questions_record.question3_intensity = 0
        questions_record.question4_intensity = 0
        questions_record.question5_intensity = 0
        questions_record.question6_intensity = 0
        questions_record.question7_intensity = 0
        questions_record.question8_intensity = 0
        questions_record.question9_intensity = 0
        questions_record.question10_intensity = 0
        questions_record.question11_intensity = 0
        questions_record.question12_intensity = 0
        questions_record.question13_intensity = 0
        questions_record.question14_intensity = 0
        questions_record.question15_intensity = 0
        questions_record.question16_intensity = 0
        questions_record.question17_intensity = 0

        questions_record.question1_frequency = 0
        questions_record.question2_frequency = 0
        questions_record.question3_frequency = 0
        questions_record.question4_frequency = 0
        questions_record.question5_frequency = 0
        questions_record.question6_frequency = 0
        questions_record.question7_frequency = 0
        questions_record.question8_frequency = 0
        questions_record.question9_frequency = 0
        questions_record.question10_frequency = 0
        questions_record.question11_frequency = 0
        questions_record.question12_frequency = 0
        questions_record.question13_frequency = 0
        questions_record.question14_frequency = 0
        questions_record.question15_frequency = 0
        questions_record.question16_frequency = 0
        questions_record.question17_frequency = 0

        form = QuestionsForm(instance=questions_record)

        user_averages = Averages.objects.get(owner_id=user_id)
        user_averages.average_intensity = 0
        user_averages.average_frequency = 0

        if form.is_valid():
            user_record = form.save(commit=False)
            user_record.owner = request.user
            user_averages.owner = request.user
            user_record.save()
            user_averages.save()

    return render(request, "app_owlwatch/test.html", {"form": form, "user_id": user_id})
