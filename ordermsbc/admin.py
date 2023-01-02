from django.contrib import admin
from .models import  ItemCard,BomAssemblyTable, Weight

# Register your models here.
admin.site.register(ItemCard)
admin.site.register(BomAssemblyTable)
admin.site.register(Weight)
