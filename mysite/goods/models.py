from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')

    def __str__(self):
        return f'{self.name} - {self.price} руб.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'