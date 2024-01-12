from django.urls import path

from survey import views

app_name = "survey"
urlpatterns = [path("", views.survey_page, name="survey_page")]
