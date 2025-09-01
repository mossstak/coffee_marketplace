from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path("admin/", admin.site.urls),

    # schema
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),

    # Swagger UI (points at api-schema)
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="swagger-ui"),
]
