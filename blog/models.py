from django.db import models
from pytils.translit import slugify
from random import choices
import string
from ckeditor_uploader.fields import RichTextUploadingField

class ArticleType(models.Model):
    name = models.CharField('Вид статьи', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = ArticleType.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(ArticleType, self).save(*args, **kwargs)

    def __str__(self):
        return f'Категория статей: {self.name}'

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"



class Article(models.Model):
    type = models.ForeignKey(ArticleType,blank=True,null=True,on_delete=models.CASCADE,verbose_name='Категория')
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_lower = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    name_slug = models.CharField(max_length=255, blank=True, null=True, db_index=True, editable=False)
    image = models.ImageField('Изображение (530 x 210)', upload_to='blog/', blank=False, null=True)
    description = RichTextUploadingField('Статья', blank=True, null=True)
    views = models.IntegerField('Просмотров', blank=True, default=0)
    is_active = models.BooleanField('Отображается на сайте?', default=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if not self.name_slug:
            testSlug = Article.objects.filter(name_slug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.name_slug = slug + slugRandom
        self.name_lower = self.name.lower()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f'Статья : {self.name} | Категория : {self.type.name}'

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)

    def get_image(self):
        if self.image:
            return self.image.url
        else:
            return ''

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статья"