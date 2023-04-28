from django.db import models
from goods.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    phone = PhoneNumberField(blank=True, verbose_name='Номер телефона', help_text='В формате: +79008007766')
    region = models.CharField(max_length=128, verbose_name='Регион')
    city = models.CharField(max_length=128, verbose_name='Город')
    street_name = models.CharField(max_length=128, verbose_name='Улица')
    house_number = models.CharField(max_length=8, verbose_name='Номер дома')
    case_number = models.CharField(max_length=8, blank=True, verbose_name='Корпус')
    apartment_number = models.CharField(max_length=8, verbose_name='Номер квартиры')
    postal_code = models.IntegerField(verbose_name='Почтовый индекс')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.id

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.price * self.quantity
