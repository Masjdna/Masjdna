from django.contrib.admin import ModelAdmin
from django.contrib.admin import site

from .models import Lecture


class LectureAdmin(ModelAdmin):
    class Meta:
        model = Lecture
        fields = "__all__"


site.register(Lecture, LectureAdmin)
