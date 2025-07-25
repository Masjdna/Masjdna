from django.db import models
from django.utils.translation import gettext as _

from masjdna.common.models import AbstractImageLinkField
from masjdna.common.models import AbstractSiteFK
from masjdna.common.models import BaseModel


class SocialMedia(
    BaseModel,
    AbstractSiteFK,
    AbstractImageLinkField,
):
    link = models.URLField(
        _("social media link"),
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Social Media")
