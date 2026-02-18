from rest_framework.generics import ListCreateAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from .models import UserCart, UserOrder, OrderItems
from .serializers import UserCartUpdateSerialzier, UserCartListCreateSerialzier, UserOrderListSerialzier, UserOrderCreateSerialzier, OrderItemsSerialzier
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from config.pagenator import MyPagenator
from rest_framework import status
# Create your views here.


class UserCartListCreateApiView(ListCreateAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartListCreateSerialzier
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagenator
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
        self.request.data['user'] = self.request.user.id
        return super().create(self.request)
    

class UserCartUpdateAPIView(UpdateAPIView):
    queryset = UserCart.objects.all()
    serializer_class = UserCartUpdateSerialzier
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagenator
    
    def partial_update(self, request, pk, *args, **kwargs):
        ser = UserCartUpdateSerialzier(data=request.data)
        ser.user = request.user
        ser.obj = self.get_object()
        msg, status_code = "Error: somthing went wrong!", status.HTTP_400_BAD_REQUEST
        if ser.is_valid(raise_exception=True):
            ser.save()
            msg, status_code = "updated successfully", status.HTTP_200_OK
        return Response({"message": msg}, status=status_code)

# =====================================================================


class UserOrderListApiView(ListAPIView):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderListSerialzier
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagenator

    def get_queryset(self):
        return self.queryset.filter(user=self.queryset.user)


class OrderCreateApiView(CreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerialzier
    permission_classes = [IsAuthenticated]



    def validate_cart_empty(self):
        carts = UserCart.objects.filter(user=self.request.user)
        if carts.exists():
            self.carts = carts
            return True
        return False

    
    def create(self, request):
        request.data['user'] = request.user.id
        ser = UserOrderCreateSerialzier(data=request.data)
        ser.user = self.request.user

        if ser.is_valid(raise_exception=True):
            validate_cart = self.validate_cart_empty()
            if not validate_cart:
                return Response({"error": "savatcha bo'sh xolatda buyurtma berib bo'lmaydi!"}, status=status.HTTP_400_BAD_REQUEST)

            ser.save()
            for cart in ser.carts:
                OrderItems.objects.create(
                    user_order=UserOrder.objects.get(id=ser.data['id']),
                    product=cart.product,
                    quantity=cart.quantity,
                    total_price=cart.product.price * cart.quantity
                )
            ser.carts.delete()
            return Response({"message": "order created successfully", "detail": ser.data})



class OrderItemsListCreateApiView(CreateAPIView):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerialzier

    