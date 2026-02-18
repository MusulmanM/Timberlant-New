from rest_framework.generics import ListCreateAPIView
from .models import Category, Product
from .serializers import CategorySerialzier, ProductSerialzier
from config.pagenator import MyPagenator
# Create your views here.


class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerialzier
    pagination_class = MyPagenator


class ProductListCreateApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialzier
    pagination_class = MyPagenator

