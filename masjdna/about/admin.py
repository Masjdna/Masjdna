from django.contrib.admin import ModelAdmin
from django.contrib.admin import site

from .models import About


class AboutAdmin(ModelAdmin):
    class Meta:
        model = About
        fields = "__all__"


site.register(About, AboutAdmin)
