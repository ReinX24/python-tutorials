from django.urls import path

from survey import views

app_name = "survey"
urlpatterns = [path("test/", views.test_page, name="test_page")]
