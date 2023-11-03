from django.db import models
from django.urls import reverse

# Create your models here.
class Cake(models.Model):
    name = models.CharField('Имя', max_length=20)
    basic = models.CharField('Бисквит', max_length=50)
    cream = models.CharField('Крем', max_length=50)
    filling = models.CharField('Начинка', max_length=50, null=True, blank=True)
    compound = models.CharField('Состав', max_length=250, null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=100, decimal_places=2)

    date = models.DateField()
    img = models.ImageField(upload_to='product_image/catalogs/classics', default='')

    slug = models.SlugField(max_length=255, unique=False, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('cake', kwargs={'cake_slug': self.slug})

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'

class Category(models.Model):
    name = models.CharField('Имя', max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'