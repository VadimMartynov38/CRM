from django.db import models
from django.utils.translation import gettext_lazy as _

class Client(models.Model):
    class TypeChoices(models.TextChoices):
        PRIVATE = "private", _("Частное лицо")
        COMPANY = "company", _("Компания")

    class StatusChoices(models.TextChoices):
        ACTIVE = "active", _("Активный")
        POTENTIAL = "potential", _("Потенциальный")
        LOST = "lost", _("Потерянный")
        BLOCKED = "blocked", _("Заблокирован")

    type = models.CharField(
        _("Тип клиента"),
        max_length=20,
        choices=TypeChoices.choices,
        default=TypeChoices.PRIVATE,
    )
    status = models.CharField(
        _("Статус"),
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.POTENTIAL,
    )

    first_name = models.CharField(_("Имя"), max_length=100, blank=True)
    last_name = models.CharField(_("Фамилия"), max_length=100, blank=True)

    company_name = models.CharField(_("Название компании"), max_length=255, blank=True)
    inn = models.CharField(_("ИНН"), max_length=20, blank=True, help_text=_("Для юрлиц"))
    kpp = models.CharField(_("КПП"), max_length=20, blank=True, help_text=_("Для юрлиц"))

    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Телефон"), max_length=50, blank=True)
    address = models.TextField(_("Адрес"), blank=True)

    notes = models.TextField(_("Примечания"), blank=True)

    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Клиент")
        verbose_name_plural = _("Клиенты")
        ordering = ["-created_at"]

    def __str__(self):
        if self.type == self.TypeChoices.COMPANY and self.company_name:
            return self.company_name
        name = f"{self.first_name} {self.last_name}".strip()
        return name if name else f"Клиент #{self.pk}"
