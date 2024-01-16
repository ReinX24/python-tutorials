from django.urls import path

from app_owlwatch import views

app_name = "app_owlwatch"
urlpatterns = [
    path("index/", views.index, name="index"),
    path("apps/", views.apps_page, name="apps_page"),
    path("test/<int:user_id>", views.test_page, name="test_page"),
    # path("test_history/<int:user_id>", views.test_history, name="test_history_page"),
]
