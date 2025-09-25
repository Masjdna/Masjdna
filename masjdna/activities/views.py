from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.shortcuts import render

from masjdna.activities.models import Activity


def all_activities(request: HttpRequest):
    site_id = get_current_site(request).id
    activities = Activity.objects.filter(site=site_id)

    return render(
        request,
        template_name="activities/all_activities.html",
        context={
            "name": get_current_site(request).name,
            "activities": activities,
        },
    )


def activity_details(request: HttpRequest, activity_id: int):
    site_id = get_current_site(request).id
    activity = Activity.objects.get(id=activity_id, site=site_id)

    return render(
        request,
        template_name="activities/activity.html",
        context={
            "name": get_current_site(request).name,
            "activity": activity,
        },
    )
