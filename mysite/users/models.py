from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя')
    phone = PhoneNumberField(blank=True, verbose_name='Номер телефона', help_text='В формате: +79008007766')
    region = models.CharField(max_length=128, verbose_name='Регион')
    city = models.CharField(max_length=128, verbose_name='Город')
    street_name = models.CharField(max_length=128, verbose_name='Улица')
    house_number = models.CharField(max_length=8, verbose_name='Номер дома')
    case_number = models.CharField(max_length=8, blank=True, verbose_name='Корпус')
    apartment_number = models.CharField(max_length=8, verbose_name='Номер квартиры')

    def __str__(self):
        return f'{self.name} | {self.phone} | {self.city}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
