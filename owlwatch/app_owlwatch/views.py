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
            }

            return render(request, "app_owlwatch/results.html", context)

    return render(request, "app_owlwatch/test.html", {"form": form, "user_id": user_id})
