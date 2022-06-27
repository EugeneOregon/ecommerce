from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Категорія')
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    showcase = models.BooleanField(default=True, verbose_name='Вітрина')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=250, verbose_name='Розмір')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Розмір'
        verbose_name_plural = 'Розміри'

    def __str__(self):
        return self.size


class Type(models.Model):
    type = models.CharField(max_length=250, verbose_name='Тип')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Типів'
        verbose_name_plural = 'Типи'

    def __str__(self):
        return self.type


class Style(models.Model):
    style = models.CharField(max_length=250, verbose_name='Стиль')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Стилів'
        verbose_name_plural = 'Стилі'

    def __str__(self):
        return self.style


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Товар')
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True, verbose_name='Опис')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    image = models.ImageField(upload_to='product', blank=True, verbose_name='Зображення')
    vendor_code = models.CharField(max_length=250, unique=True, verbose_name='Артикул')
    stock = models.IntegerField(verbose_name='Кількість, шт.')
    available = models.BooleanField(default=True, verbose_name='Наявність')
    showcase = models.BooleanField(default=True, verbose_name='Вітрина')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    size = models.ManyToManyField(Size, verbose_name='Розмір')
    type = models.ManyToManyField(Type, verbose_name='Тип')
    style = models.ManyToManyField(Style, verbose_name='Стиль')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товари'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Слайдер')
    image = models.ImageField(upload_to='slider', blank=True, verbose_name='Зображення')
    published = models.BooleanField(default=True, verbose_name='Опубліковано')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        db_table = 'Cart'

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product
