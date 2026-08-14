from django.db import models
from django.utils.translation import gettext_lazy as _

class Campaign(models.Model):
    name = models.CharField(_("Название кампании"), max_length=255)
    description = models.TextField(_("Описание"), blank=True)
    budget = models.DecimalField(_("Бюджет"), max_digits=12, decimal_places=2, default=0)
    start_date = models.DateField(_("Дата начала"))
    end_date = models.DateField(_("Дата окончания"))
    status = models.CharField(
        _("Статус"),
        max_length=50,
        choices=[
            ("draft", _("Черновик")),
            ("active", _("Активна")),
            ("paused", _("На паузе")),
            ("completed", _("Завершена")),
        ],
        default="draft",
    )

    created_at = models.DateTimeField(_("Дата создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Дата обновления"), auto_now=True)

    class Meta:
        verbose_name = _("Рекламная кампания")
        verbose_name_plural = _("Рекламные кампании")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
