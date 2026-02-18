from django.contrib import admin
from .models import User, UserAddress, UserFavourite
# Register your models here.


admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(UserFavourite)