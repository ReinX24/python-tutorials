from django.urls import path

from app_owlwatch import views

app_name = "app_owlwatch"
urlpatterns = [
    path("", views.index, name="index"),
    path("apps/", views.apps_page, name="apps_page"),
    path("test/<int:user_id>/", views.test_page, name="test_page"),
    path("test_reset/<int:user_id>/", views.test_reset, name="test_reset"),
]
