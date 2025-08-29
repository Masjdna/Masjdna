from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.shortcuts import render

from masjdna.activities.models import Activity
from masjdna.lectures.models import Lecture
from masjdna.services.models import Services

from .models import About


def about(request: HttpRequest):
    about_record = About.objects.get(site=get_current_site(request).id)
    activities = Activity.objects.filter(site=get_current_site(request).id).order_by(
        "-id",
    )[:3]
    lectures = Lecture.objects.all()
    services_records = Services.objects.filter(site=get_current_site(request).id)

    return render(
        request,
        template_name="pages/about.html",
        context={
            "name": get_current_site(request).name,
            "about_overview": about_record.intro,
            "about_image": about_record.image_link.url,
            "services": services_records,
            "activities": activities,
            "lectures": lectures,
        },
    )
