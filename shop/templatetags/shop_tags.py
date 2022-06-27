from django import template

from shop.models import *

register = template.Library()

menu = [
    {'title': 'Каталог', 'url_name': 'groups'},
    {'title': 'Контакти', 'url_name': 'anyway'},
    {'title': 'Кошик', 'url_name': 'cart_detail'},
]

footer = [
    {'title': 'Доставка', 'url_name': 'anyway'},
    {'title': 'Контакти', 'url_name': 'anyway'},
    {'title': 'Про нас', 'url_name': 'anyway'},
]


@register.simple_tag()
def get_points():
    return menu


@register.simple_tag()
def get_footer_points():
    return footer


@register.simple_tag()
def get_categories():
    return Category.objects.filter(showcase=True)[:3]


@register.simple_tag()
def get_random_products():
    return Product.objects.all()[:4]


@register.simple_tag()
def get_slider():
    return Slider.objects.filter(published=True)


@register.inclusion_tag('include/tags/categories.html')
def get_all_categories():
    categories = Category.objects.filter(showcase=True)
    return {"categories": categories}
