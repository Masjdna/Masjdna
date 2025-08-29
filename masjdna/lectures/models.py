from django.db import models
from django.utils.translation import gettext as _

from masjdna.common.models import AbstractSiteFK
from masjdna.common.models import BaseModel


class Lecture(
    BaseModel,
    AbstractSiteFK,
):
    lecturer = models.CharField(verbose_name=_("Lecturer"))
    day = models.CharField(verbose_name=_("Day"))
    name = models.CharField(verbose_name=_("Name"))
    time = models.CharField(verbose_name=_("Time"))

    class Meta:
        verbose_name = _("Lectures")
