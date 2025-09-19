from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
from django.shortcuts import render

from masjdna.services.models import Services


def all_services(request: HttpRequest):
    site_id = get_current_site(request).id
    services_records = Services.objects.filter(site=site_id)

    return render(
        request,
        template_name="services/all_services.html",
        context={
            "name": get_current_site(request).name,
            "services": services_records,
        },
    )
