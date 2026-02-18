from django.urls import path
from . import views



urlpatterns = [
    path('category/', views.CategoryListCreateApiView.as_view()),
    path('product/', views.ProductListCreateApiView.as_view()),
]
