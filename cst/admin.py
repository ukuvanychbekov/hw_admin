from django.contrib import admin
from .models import *


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_sale'
    empty_value_display = 'пустой'
    search_fields = ('owner_name',)
    list_editable = ('date_sale',)
    list_display = ('owner_name', 'date_sale', 'status', 'total_space', 'get_cost',)

    @admin.display(description='Общая стоимость')
    def get_cost(self, obj):
        return obj.total_space * obj.block.cost


class BlockAdmin(admin.ModelAdmin):
    empty_value_display = 'пустой'
    list_display = ('number', 'porch', 'floor', 'flat_on_floor', 'total_float', 'total_cost', )

    @admin.display(description='Общее кол-во квартир')
    def total_float(self, obj):
        return obj.floor * obj.flat_on_floor

    @admin.display(description='Итоговая стоимость')
    def total_cost(self, obj):
        flats = Flat.objects.filter(block=obj)
        final_price = 0
        for flat in flats:
            final_price += flat.total_space * obj.cost * obj.cost
        return final_price


admin.site.register(Block, BlockAdmin)

