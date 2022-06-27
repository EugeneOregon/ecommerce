from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('filter/', views.FilterProductView.as_view(), name='filter'),
    path('groups/', views.GroupsView.as_view(), name='groups'),
    path('anyway/', views.anyway, name='anyway'),
    path("<slug:slug>/", views.ProductDetailView.as_view(), name="product_detail"),
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),

]
