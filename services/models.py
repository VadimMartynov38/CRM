from django.db import models

class Service(models.Model):
    name = models.CharField("Название услуги", max_length=255, unique=True)
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Стоимость", max_digits=10, decimal_places=2)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name
