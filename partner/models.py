from django.db import models

class Partner(models.Model):
    name = models.CharField('Название партнера', max_length=255, blank=False, null=True)
    image = models.ImageField('Лого (136 x ??)', upload_to='partner/', blank=False, null=True)
    description = models.CharField('Описание', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Партнер: {self.name}'

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

class Unit(models.Model):
    price_item = models.ManyToManyField(Partner, verbose_name='Относится к партнеру', related_name='units')
    name = models.CharField('Совместная работа', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Совместная работа: {self.name}'

    class Meta:
        verbose_name = "Совместная работа"
        verbose_name_plural = "Совместные работы"
