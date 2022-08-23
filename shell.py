from datetime import date

from cst.models import *

b1 =Block.objects.create(number=1, cost=500, )


class Block(models.Model):
    number = models.IntegerField(unique=True)
    cost = models.IntegerField()
    porch = models.IntegerField()
    floor = models.IntegerField()
    flat_on_floor = models.IntegerField()


class Flat(models.Model):
    owner_name = models.CharField(max_length=100, null=True, blank=True)
    date_sale = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    total_space = models.IntegerField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
