from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    CurrentUserView,
    CartItemListCreateView,
    RoleAwareTokenView
)

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name="user-list"),
    path('users/<int:pk>/', UserDetailView.as_view(), name="user-detail"),
    path('users/me/', CurrentUserView.as_view(), name="current-user"),
    path('cart/', CartItemListCreateView.as_view(), name="cart-list"),
    path('token/', RoleAwareTokenView.as_view(), name="token_obtain_pair"),
]