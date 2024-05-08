# Generated by Django 4.2.11 on 2024-05-03 20:26

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Атрибут')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя группы')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=295)),
                ('description', models.TextField(blank=True, null=True)),
                ('meta_title', models.CharField(max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=255, null=True)),
                ('meta_keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('seo_keyword', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, max_length=300, null=True, upload_to='catalog/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=299, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False, null=True)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False, null=True)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False, null=True)),
                ('level', models.PositiveIntegerField(editable=False, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фильтр')),
            ],
        ),
        migrations.CreateModel(
            name='FilterGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя группы')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=300, null=True, upload_to='catalog/')),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=299)),
                ('description', models.TextField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=255)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=300, null=True, upload_to='catalog/')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=299, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True, verbose_name='Скидка в %')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('manufacturer', models.ForeignKey(max_length=300, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer')),
                ('stock_status_id', models.ForeignKey(max_length=300, on_delete=django.db.models.deletion.CASCADE, to='products.stockstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, max_length=300, null=True, upload_to='catalog/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.filter')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.AddField(
            model_name='filter',
            name='filter_group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.filtergroup'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.attributegroup'),
        ),
    ]
