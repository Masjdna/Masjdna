from django.db import models
from django.utils.translation import gettext as _


class AbstractImageLinkField(models.Model):
    image_link = models.ImageField(
        _("image link"),
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        abstract = True
