from django.contrib import admin
from orders.models import Order,Orderitem
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter=[
        "owner",
        "order_status",
        "created_at",
    ]
    search_fields=(
        "owner",
        "id",
    )    

admin.site.register(Order,OrderAdmin)





# it shows all the order details in admin panel
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'owner', 'order_status', 'total_price', 'created_at', 'updated_at')

#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)