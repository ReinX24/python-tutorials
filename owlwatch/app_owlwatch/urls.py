from django.urls import path

from app_owlwatch import views

app_name = "app_owlwatch"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("apps/", views.apps_page, name="apps_page"),
    path("test/", views.test_page, name="test_page"),
]
