from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Contract(models.Model):
    class TypeChoices(models.TextChoices):
        SUPPLY = "supply", _("Поставка")
        SERVICE = "service", _("Оказание услуг")
        LICENSE = "license", _("Лицензия/подписка")
        OTHER = "other", _("Другое")

    class StatusChoices(models.TextChoices):
        DRAFT = "draft", _("Черновик")
        SIGNED = "signed", _("Подписан")
        ACTIVE = "active", _("Активен")
        COMPLETED = "completed", _("Завершен")
        CANCELLED = "cancelled", _("Расторгнут")

    number = models.CharField(_("Номер договора"), max_length=100, unique=True)
    title = models.CharField(_("Название/предмет"), max_length=255)
    type = models.CharField(
        _("Тип договора"),
        max_length=20,
        choices=TypeChoices.choices,
        default=TypeChoices.OTHER,
    )
    status = models.CharField(
        _("Статус"),
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.DRAFT,
    )
    amount = models.DecimalField(
        _("Сумма"),
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
    )
    currency = models.CharField(_("Валюта"), max_length=3, default="RUB")

    start_date = models.DateField(_("Дата начала"), null=True, blank=True)
    end_date = models.DateField(_("Дата окончания"), null=True, blank=True)

    file = models.FileField(_("Файл договора"), upload_to="contracts/", blank=True, null=True)
    notes = models.TextField(_("Примечания"), blank=True)

    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Договор")
        verbose_name_plural = _("Договоры")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.number} — {self.title}"
