from django.urls import path

from owl_watch import views

app_name = "owl_watch"
urlpatterns = [path("test/", views.test_page, name="test_page")]
