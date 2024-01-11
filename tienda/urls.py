from .views import (
    ProductoListView,
    CreateProductoView,
    UpdateProductoView,
    DeleteProductoView,
    ProductoDetailView,
)
from django.urls import path

urlpatterns = [
    path(
        "tienda/admin/productos/listado",
        ProductoListView.as_view(),
        name="producto_list",
    ),
    path(
        "tienda/admin/productos/crear",
        CreateProductoView.as_view(),
        name="producto_create",
    ),
    path(
        "tienda/admin/productos/editar/<int:pk>",
        UpdateProductoView.as_view(),
        name="producto_update",
    ),
    path(
        "tienda/admin/productos/eliminar/<int:pk>",
        DeleteProductoView.as_view(),
        name="producto_delete",
    ),
    path(
        "tienda/admin/productos/detalle/<int:pk>",
        ProductoDetailView.as_view(),
        name="producto_detail",
    ),
]
