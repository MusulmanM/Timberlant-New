from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('v1/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-address/', views.UserAddressListCreateApiView.as_view()),
    path('user-address/<int:pk>', views.UserAddressDestorApiView.as_view()),
    path('user-favourite/', views.UserFavouriteListCreateApiView.as_view()),
    path('user-favourite/<int:pk>', views.Userfavouritedestorapiview.as_view()),
]
