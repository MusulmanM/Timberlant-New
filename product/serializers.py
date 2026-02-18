from rest_framework.serializers import ModelSerializer
from .models import Category, Product


class CategorySerialzier(ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
    

class ProductSerialzier(ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        