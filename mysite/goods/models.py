from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена товара')

    def __str__(self):
        return f'{self.name} - {self.price} руб.'


