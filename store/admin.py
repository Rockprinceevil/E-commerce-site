from django.contrib import admin

from .models import *

class OrderInline(admin.TabularInline): # new
	model = Order
class CustomerAdmin(admin.ModelAdmin):
	inlines = [
			OrderInline,
	]

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)