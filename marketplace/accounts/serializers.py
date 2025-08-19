from rest_framework import serializers
from .models import User, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'quantity', 'unit_price', 'add_at']


class UserSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'role',
            'phone_number',
            'address',
            'cart_item',
            'is_admin',
            'is_seller',
            'is_customer'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data.get('role', 'CUSTOMER'),
            phone_number=validated_data.get('phone_number', ''),
            address=validated_data.get('address', '')
        )
        return user
