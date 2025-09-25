from django.urls import path

from .views import activity_details
from .views import all_activities

app_name = "activities"

urlpatterns = [
    path("all_activites/", all_activities, name="all_activities"),
    path("activity/<int:activity_id>/", activity_details, name="activity_details"),
]
