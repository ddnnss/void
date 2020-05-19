from django.db import models

# class PriceItem(models.Model):
#     name = models.CharField('Название тарифа', max_length=255, blank=False, null=True)
#
#
#
# class Unit(models.Model):
#     price_item = models.ManyToManyField(PriceItem, verbose_name='Относится к тарифу')
#     name = models.CharField('Название элемента тарифа', max_length=255, blank=False, null=True)