from django.db import models
from user.models import User, UserAddress
from product.models import Product

# Create your models here.


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} | {self.product} | {self.quantity}"


class OrderPaymentType(models.TextChoices):
    CASH = 'cash', "Naqd pul"
    CLICK = 'click', "Click orqali"
    PAYME = 'payme', "Payme orqali"
    CART = 'cart', "Plastik orqali"
    OTHER = 'other', "boshqa tolov turi orqali"

class OrderStatus(models.TextChoices):
    NEW = 'new', 'Yangi buyurtma'
    WAITING = 'waiting', 'Kutulmoqda...'
    IN_PROGRESS = 'in_progress', 'Jarayonda...'
    WAITING_PAY = 'waiting_pay', 'Tolov qilish Kutilmoqda...'
    DELIVERING = 'delivering', 'Yetkazib berilmoqda...'
    DELIVERIED = 'deliveried', 'Yetkazib berilgan.'
    COMPLETED = 'complated', 'Tugallangan.'
    CANCALLED_BY_CUSTOMER = 'cancalled_by_customer', 'Mijoz tomondan bekor qilingan'
    CANCALLED_BY_SELLER = 'cancalled_by_seller', 'Sotuvchi tomonidan bekor qilingan'

class UserOrder(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(UserAddress, on_delete=models.SET_NULL, null=True)
    total_price = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    payment_type = models.CharField(max_length=50, choices=OrderPaymentType.choices)
    status = models.CharField(max_length=50, choices=OrderStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user}"
    
    

class OrderItems(models.Model):
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.PositiveSmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user_order.user} | {self.product} | {self.quantity}"
