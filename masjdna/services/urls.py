from django.urls import path

from .views import all_services

app_name = "services"

urlpatterns = [
    path("all_services/", view=all_services, name="all_services"),
]
