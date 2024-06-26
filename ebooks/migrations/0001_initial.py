# Generated by Django 5.0.4 on 2024-04-27 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('publication_date', models.DateField()),
                ('num_pages', models.PositiveIntegerField(blank=True, null=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('authors', models.ManyToManyField(blank=True, null=True, related_name='author_ebooks', to='ebooks.author')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_ebooks', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(blank=True, null=True, related_name='genre_ebooks', to='ebooks.genre')),
            ],
            options={
                'verbose_name_plural': 'Ebook',
            },
        ),
    ]
