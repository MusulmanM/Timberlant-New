from django.urls import path
from . import views



urlpatterns = [
    path('user-cart/', views.UserCartListCreateApiView.as_view()),
    path('user-cart/update/<int:pk>/', views.UserCartUpdateAPIView.as_view()),
    path('user-order/', views.UserOrderListApiView.as_view()),
    path('order-items/', views.OrderItemsListCreateApiView.as_view()),
]
