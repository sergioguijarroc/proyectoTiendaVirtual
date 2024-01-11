from django.shortcuts import render
from .models import User, Producto, Marca, Compra
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy

# Create your views here.


class ProductoListView(ListView):
    model = Producto
    template_name = "tienda/producto_list.html"


class CreateProductoView(CreateView):
    model = Producto
    template_name = "tienda/producto_create.html"
    fields = "__all__"
    success_url = reverse_lazy("producto_list")


class UpdateProductoView(UpdateView):
    model = Producto
    template_name = "tienda/producto_update.html"
    fields = "__all__"
    success_url = reverse_lazy("producto_list")


class DeleteProductoView(DeleteView):
    model = Producto
    template_name = "tienda/producto_delete.html"
    success_url = reverse_lazy("producto_list")


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "tienda/producto_detail.html"
