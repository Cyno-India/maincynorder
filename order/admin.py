from django.contrib import admin
from .models import  MasterModel, Order, MasterDocs, Docs

# Register your models here.
admin.site.register(Order)
admin.site.register(MasterModel)
admin.site.register(MasterDocs)
admin.site.register(Docs)




