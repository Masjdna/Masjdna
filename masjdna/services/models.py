from django.db import models
from django.utils.translation import gettext as _

from masjdna.common.models import AbstractImageLinkField
from masjdna.common.models import AbstractSiteFK
from masjdna.common.models import BaseModel


class Services(
    BaseModel,
    AbstractSiteFK,
    AbstractImageLinkField,
):
    description = models.TextField(verbose_name=_("Service Description"))

    class Meta:
        verbose_name = _("Services")
