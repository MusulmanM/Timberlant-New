from django.contrib import admin
from .models import UserOrder, OrderItems, UserCart
# Register your models here.


admin.site.register(UserCart)
admin.site.register(UserOrder)
admin.site.register(OrderItems)
