from rest_framework.serializers import ModelSerializer
from .models import UserAddress, UserFavourite


class UserAddressSerialzier(ModelSerializer):
    
    class Meta:
        model = UserAddress
        fields = '__all__'
    

class UserFavouriteSerialzier(ModelSerializer):
    
    class Meta:
        model = UserFavourite
        fields = '__all__'
        