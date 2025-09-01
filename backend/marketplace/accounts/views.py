from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import CartItem
from .serializers import UserSerializer, CartItemSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt import RoleAwareTokenObtainPairSerializer
from .permissions import IsSelfOrAdmin, IsCustomer

User = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    """
    List all users (admin only) or register a new user (open to anyone).
    GET /users/   -> admin only
    POST /users/  -> public registration
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific user.
    - Users can manage their own account
    - Admins can manage any account
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSelfOrAdmin]


class CurrentUserView(generics.RetrieveAPIView):
    """
    Get the currently logged-in user.
    GET /users/me/ -> returns the authenticated user's data
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self): return self.request.user


class CartItemListCreateView(generics.ListCreateAPIView):
    """
     View or add items to the logged-in customer's cart.
        - Customers only
        - Each user only sees their own cart
    """
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RoleAwareTokenView(TokenObtainPairView):
    """
    Custom JWT token endpoint that includes the user's role and username
    in the JWT payload.
    """
    serializer_class = RoleAwareTokenObtainPairSerializer
