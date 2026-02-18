from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import UserCart, UserOrder, OrderItems
from rest_framework.exceptions import ValidationError

class UserCartListCreateSerialzier(ModelSerializer):
    
    class Meta:
        model = UserCart
        fields = '__all__'
        read_only_fields = ("quantity", "created_at", "updated_at")


class UserCartUpdateSerialzier(ModelSerializer):
    
    class Meta:
        model = UserCart
        fields = '__all__'
        read_only_fields = ("user", "product", "created_at", "updated_at")
    
    def validate_quantity(self, value):
        if value > 50:
            raise ValidationError("Siz 50 tadan ko'p birdaniga qo'sha olmaysiz!")
        return value
    
    def validate_user(self, value):
        if self.user != self.obj.user:
            raise ValidationError("Siz birovni savatchasini o'zgartira olmaysiz!")
        return value

    

class UserOrderListSerialzier(ModelSerializer):
    order_item = SerializerMethodField(read_only=True)
    
    class Meta:
        model = UserOrder
        fields = '__all__'


    def get_order_items(self, obj):
        return OrderItemsSerialzier(obj.order_items.all(), many=True).data

        

class UserOrderCreateSerialzier(ModelSerializer):
    order_items = SerializerMethodField(read_only=True)
    order_items_data= []
    
    class Meta:
        model = UserOrder
        fields = '__all__'
        extra_kwargs = {
            'address': {'required': True}
        }
        
    def validate_cart(self, user):
        carts = UserCart.objects.filter(user=user)
        if not carts.exists():
            raise ValidationError("Sizda savatcha bo'sh")
        self.carts = carts
        
        
    def validate_address(self, value):
        self.validate_cart(self.user)
        if value.user != self.user:
            raise ValidationError("Siz o'zingizning manzilingizga buyurtma berolasiz holos!")
        return value

    
    
class OrderItemsSerialzier(ModelSerializer):
    
    class Meta:
        model = OrderItems
        fields = '__all__'
