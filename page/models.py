from django.db import models

class Callback(models.Model):
    user_phone = models.CharField('Телефон', max_length=255, blank=False)
    name = models.CharField('Имя',blank=True,max_length=255,null=True)
    created_at = models.DateTimeField('Дата заполнения', auto_now_add=True)
    is_done = models.BooleanField('Обработана?', default=False)

    def __str__(self):
        return f'Заказ звонка. От : {self.user_phone}. Дата создания :{self.created_at}'

    class Meta:
        verbose_name = "Форма заказа звонка"
        verbose_name_plural = "Формы заказа звонка"