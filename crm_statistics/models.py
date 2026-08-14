from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class DailyReport(models.Model):
    date = models.DateField(_("Дата"), unique=True)
    leads_count = models.PositiveIntegerField(_("Лиды"), default=0)
    clients_count = models.PositiveIntegerField(_("Клиенты"), default=0)
    contracts_count = models.PositiveIntegerField(_("Контракты"), default=0)
    campaigns_count = models.PositiveIntegerField(_("Кампании"), default=0)

    revenue = models.DecimalField(
        _("Выручка"), max_digits=12, decimal_places=2, default=0
    )
    avg_contract_value = models.DecimalField(
        _("Средний чек контракта"), max_digits=10, decimal_places=2, default=0
    )

    created_at = models.DateTimeField(_("Создан"), auto_now_add=True)
    updated_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name=_("Обновлено кем")
    )

    class Meta:
        verbose_name = _("Ежедневный отчёт")
        verbose_name_plural = _("Ежедневные отчёты")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date}: выручка {self.revenue} ₽"
