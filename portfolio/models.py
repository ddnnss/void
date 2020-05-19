from django.db import models

class PortfolioItem(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение (432 x 432)', upload_to='portfoliio/', blank=False, null=True)
    description = models.CharField('Описание', max_length=255, blank=False, null=True)

    def __str__(self):
        return f'Элемент портфолио : {self.name}'

    class Meta:
        verbose_name = "Элемент портфолио"
        verbose_name_plural = "Элементы портфолио"

    def save(self, *args, **kwargs):
       temp_name = self.name.split(' ')
       word = f'<em>{temp_name.pop()}</em>'
       temp_name.append(word)
       self.name = ' '.join(temp_name)
       super(PortfolioItem, self).save(*args, **kwargs)

class PortfolioItemImage(models.Model):
    item = models.ForeignKey(PortfolioItem,blank=True,null=True,on_delete=models.CASCADE,verbose_name='Элемент портфолио', related_name='images')
    image_2000 = models.ImageField('Изображение (2200)', upload_to='portfoliio/', blank=False, null=True)
    image_1000 = models.ImageField('Изображение (1100)', upload_to='portfoliio/', blank=False, null=True)

    def __str__(self):
        return f'Фото для элемента портфолио : {self.item.name}'

    class Meta:
        verbose_name = "Фото для элемента портфолио"
        verbose_name_plural = "Фото для элемента портфолио"