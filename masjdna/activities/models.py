from django.db import models
from django.utils.translation import gettext as _

from masjdna.common.models import AbstractImageLinkField
from masjdna.common.models import AbstractSiteFK
from masjdna.common.models import BaseModel


# todo: change one image into many images using new Model
class Activity(
    BaseModel,
    AbstractSiteFK,
    AbstractImageLinkField,
):
    header = models.TextField(verbose_name=_("Activity Header"))
    activity_description = models.TextField(verbose_name=_("Activity Description"))

    class Meta:
        verbose_name = _("Activity")
