from django.urls import path, include

from journal import views

app_name = "journal"
urlpatterns = [
    path("entries/<int:user_id>/", views.entries, name="entries"),
    path("add_entry/<int:user_id>/", views.add_entry, name="add_entry"),
    path("entry_info/<int:entry_id>/", views.entry_info, name="entry_info"),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name="edit_entry"),
    path("delete_entry/<int:entry_id>/", views.delete_entry, name="delete_entry"),
]
