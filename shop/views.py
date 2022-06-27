from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


class SizeTypeStyle:
    @staticmethod
    def get_sizes():
        return Size.objects.all()

    @staticmethod
    def get_types():
        return Type.objects.all()

    @staticmethod
    def get_styles():
        return Style.objects.all()


class Home(SizeTypeStyle, ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(available=True, showcase=True)[:8]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Взуттєво, що не кажи'
        return context


# class ProductView(SizeTypeStyle, ListView):
#     paginate_by = 8
#     model = Product
#     queryset = Product.objects.filter(available=True)


class ProductDetailView(SizeTypeStyle, DetailView):
    model = Product
    slug_field = "slug"


class CategoryView(SizeTypeStyle, ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True)


class GroupsView(SizeTypeStyle, ListView):
    paginate_by = 8
    model = Product
    template_name = 'shop/groups.html'

    def get_queryset(self):
        return Product.objects.filter(available=True)


class FilterProductView(SizeTypeStyle, ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(size__in=self.request.GET.getlist("size")) |
            Q(type__in=self.request.GET.getlist("type")) |
            Q(style__in=self.request.GET.getlist("style"))
        )
        return queryset


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    return redirect('cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'shop/cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


def anyway(request):
    return render(request, 'shop/anyway.html')
