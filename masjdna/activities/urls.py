from django.urls import path

from .views import all_activities

app_name = "activities"

urlpatterns = [
    path("all_activites/", all_activities, name="all_activities"),
]
