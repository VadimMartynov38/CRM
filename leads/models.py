from django.db import models
from django.utils.translation import gettext_lazy as _

class Lead(models.Model):
    class StatusChoices(models.TextChoices):
        NEW = "new", _("Новый")
        CONTACTED = "contacted", _("Контактировали")
        QUALIFIED = "qualified", _("Квалифицирован")
        CONVERTED = "converted", _("Конвертирован")
        LOST = "lost", _("Утерян")

    class SourceChoices(models.TextChoices):
        WEBSITE = "website", _("Сайт (форма)")
        SOCIAL = "social", _("Соцсети")
        AD = "ad", _("Реклама")
        REFERRAL = "referral", _("Реферал")
        OTHER = "other", _("Другое")

    first_name = models.CharField(_("Имя"), max_length=100)
    last_name = models.CharField(_("Фамилия"), max_length=100, blank=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Телефон"), max_length=50, blank=True)
    source = models.CharField(
        _("Источник"),
        max_length=20,
        choices=SourceChoices.choices,
        default=SourceChoices.WEBSITE,
    )
    status = models.CharField(
        _("Статус"),
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )
    notes = models.TextField(_("Заметки"), blank=True)

    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Лид")
        verbose_name_plural = _("Лиды")
        ordering = ["-created_at"]

    def __str__(self):
        name = f"{self.first_name} {self.last_name}".strip()
        return name if name else f"Лид #{self.pk}"
