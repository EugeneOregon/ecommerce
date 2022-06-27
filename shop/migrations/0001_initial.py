# Generated by Django 4.0.4 on 2022-06-24 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cart',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Категорія')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='category')),
                ('showcase', models.BooleanField(default=True, verbose_name='Вітрина')),
            ],
            options={
                'verbose_name': 'Категорію',
                'verbose_name_plural': 'Категорії',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=250, verbose_name='Розмір')),
            ],
            options={
                'verbose_name': 'Розмір',
                'verbose_name_plural': 'Розміри',
                'ordering': ('size',),
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Слайдер')),
                ('image', models.ImageField(blank=True, upload_to='slider', verbose_name='Зображення')),
                ('published', models.BooleanField(default=True, verbose_name='Опубліковано')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=250, verbose_name='Стиль')),
            ],
            options={
                'verbose_name': 'Стилів',
                'verbose_name_plural': 'Стилі',
                'ordering': ('style',),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Типів',
                'verbose_name_plural': 'Типи',
                'ordering': ('type',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Товар')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('image', models.ImageField(blank=True, upload_to='product', verbose_name='Зображення')),
                ('vendor_code', models.CharField(max_length=250, unique=True, verbose_name='Артикул')),
                ('stock', models.IntegerField(verbose_name='Кількість, шт.')),
                ('available', models.BooleanField(default=True, verbose_name='Наявність')),
                ('showcase', models.BooleanField(default=True, verbose_name='Вітрина')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категорія')),
                ('size', models.ManyToManyField(to='shop.size', verbose_name='Розмір')),
                ('style', models.ManyToManyField(to='shop.style', verbose_name='Стиль')),
                ('type', models.ManyToManyField(to='shop.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Товари',
                'verbose_name_plural': 'Товари',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
    ]