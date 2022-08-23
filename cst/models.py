from django.db import models


class Block(models.Model):
    number = models.IntegerField(unique=True, verbose_name='Номер блока')
    cost = models.IntegerField(verbose_name='Цена за квадратный метр')
    porch = models.IntegerField(verbose_name='Кол-во подъездов')
    floor = models.IntegerField(verbose_name='Кол-во этажей')
    flat_on_floor = models.IntegerField(verbose_name='Кол-во квартир на этаже')


    def __str__(self):
        return f'Номер блока {self.number}'


class Flat(models.Model):
    vykup ='v'
    vykup_ne_do_konca ='vn'
    rast ='r'
    ne_prod ='n'
    status = [(vykup,"Выкуп"), (vykup_ne_do_konca,"Выкуп не до конца"), (rast,"Расторгнуто"), (ne_prod,"Не продано"),]
    status = models.CharField(max_length=50, choices=status, verbose_name='Статус сделки')
    owner_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Покупатель')
    date_sale = models.DateField(null=True, blank=True, verbose_name='Дата продажи')
    total_space = models.IntegerField(verbose_name='Общая площадь')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, verbose_name='Номер Блока')

    def __str__(self):
        return f'Квартира {self.status} в блоке {self.block}'



