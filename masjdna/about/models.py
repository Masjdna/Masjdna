from django.db import models
from django.utils.translation import gettext as _

from masjdna.common.models import AbstractImageLinkField
from masjdna.common.models import AbstractSiteFK
from masjdna.common.models import BaseModel


class About(
    BaseModel,
    AbstractSiteFK,
    AbstractImageLinkField,
):
    intro = models.TextField(verbose_name=_("Intro"))

    class Meta:
        verbose_name = _("About")
