# Generated by Django 3.1.7 on 2021-02-24 17:31

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priopity', models.PositiveIntegerField(default=2, validators=[django.core.validators.MaxLengthValidator(100.0)])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(post.models.LikeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=128, unique=True)),
                ('priopity', models.PositiveIntegerField(default=2, validators=[django.core.validators.MaxLengthValidator(100.0)])),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
            bases=(post.models.LikeMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=128)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('content', models.TextField(max_length=4096)),
                ('priopity', models.PositiveIntegerField(default=2, validators=[django.core.validators.MaxLengthValidator(100.0)])),
                ('likes', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.author')),
                ('tags', models.ManyToManyField(to='post.Tag')),
            ],
            bases=(post.models.LikeMixin, models.Model),
        ),
    ]
