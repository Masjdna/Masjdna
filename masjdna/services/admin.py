from django.contrib.admin import ModelAdmin
from django.contrib.admin import site

from .models import Services


class ServicesAdmin(ModelAdmin):
    class Meta:
        model = Services
        fields = "__all__"


site.register(Services, ServicesAdmin)
