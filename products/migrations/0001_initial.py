# Generated by Django 4.0.4 on 2022-11-18 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='images/categories', verbose_name='avatar')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='images/categories', verbose_name='avatar')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='products.category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'producst',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='images/files', verbose_name='file')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'files',
            },
        ),
    ]
