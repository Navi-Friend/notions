from django.urls import path

from . import views

app_name = "notion"

urlpatterns = [
    path("notion-list/", views.notion_list, name="notion_list")
]
