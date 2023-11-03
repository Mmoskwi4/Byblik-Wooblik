from django.db import models

# Create your models here.
class Completed(models.Model):
    name = models.CharField('Имя', max_length=20)
    basic = models.CharField('Бисквит', max_length=50)
    cream = models.CharField('Крем', max_length=50)
    filling = models.CharField('Начинка', max_length=50, null=True)
    price = models.DecimalField('Цена', max_digits=100, decimal_places=2)
    text = models.TextField('Описание', max_length=256)

    date = models.DateTimeField()
    img = models.ImageField(upload_to='product_image/completed_works', default='', )

    def __str__(self):
        return f"{self.date} - {self.name}"

    class Meta:
        verbose_name = 'Готовая работа'
        verbose_name_plural = 'Готовые работы'