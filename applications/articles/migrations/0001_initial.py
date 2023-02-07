# Generated by Django 4.1.6 on 2023-02-06 03:25

import ckeditor.fields
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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=60)),
                ('content', ckeditor.fields.RichTextField()),
                ('urlToImage', models.URLField(max_length=255)),
                ('publishedAt', models.DateField(auto_now=True, verbose_name='Publication Date')),
                ('status', models.BooleanField(default=True, verbose_name='Published/No Published')),
                ('article_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.category', verbose_name='Category')),
            ],
        ),
    ]