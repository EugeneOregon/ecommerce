from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'price', 'stock', 'showcase', 'available')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('available', 'showcase', 'category')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('showcase', 'available')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'showcase')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('showcase',)
    list_editable = ('showcase',)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('published',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')
    list_display_links = ('id', 'size')
    search_fields = ('size',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type')
    list_display_links = ('id', 'type')
    search_fields = ('type',)


class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'style')
    list_display_links = ('id', 'style')
    search_fields = ('style',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Style, StyleAdmin)
