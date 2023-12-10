from django.contrib import admin
from .models import *

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('customer', 'price', 'created')
    search_fields = ('customer', 'price')

admin.site.register(Product)
admin.site.register(Producer)
admin.site.register(Statement)
admin.site.register(StatementProduct)
