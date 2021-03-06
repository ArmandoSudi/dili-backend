# Generated by Django 2.1.15 on 2020-05-19 13:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iso_code', models.CharField(max_length=3)),
                ('label', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('post_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_brand', models.CharField(max_length=100)),
                ('product_model', models.CharField(max_length=100)),
                ('prodcut_price', models.IntegerField()),
                ('product_description', models.CharField(max_length=250)),
                ('thumbnail_url', models.URLField(blank=True, default='http://via.placeholder.com/140x100')),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('views', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('longitude', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.Category')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Currency')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Location')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_uid', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('avatar_url', models.URLField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.Location')),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.UserType'),
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.User'),
        ),
    ]
