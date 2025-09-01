from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSeller(BasePermission):
    """ Only Allow access to if user is a seller """

    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_seller


class IsCustomer(BasePermission):
    """ Only Allow access if the user is a customer """

    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_customer


class IsAdmin(BasePermission):
    """ Only Allow access if the user is an admin """

    def has_permission(self, request, view):
        if request.method == SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_admin


class IsSelfOrAdmin(BasePermission):
    """Allow users to access their own data, or admins everything """

    def has_object_permission(self, request, view, obj):
        if request.method == SAFE_METHODS:
            return True
        return request.user.is_authenticated and (
            request.user.is_admin or obj == request.user
        )

class IsSellerForWriteAndOwner(BasePermission):
    """
    - Everyone can read products
    - Only sellers can create
    - Only the seller-owner of a product can update/delete it
    """
    def has_permission(self, request, view):
        # Anyone can read
        if request.method in SAFE_METHODS:
            return True
        # Only sellers can write
        return request.user.is_authenticated and getattr(request.user, "role", None) == "seller"

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # Only the owner-seller can modify
        return obj.seller_id == request.user.id
