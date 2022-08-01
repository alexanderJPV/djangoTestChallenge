# Generated by Django 4.0.6 on 2022-07-31 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('ci', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('addres', models.CharField(max_length=255)),
                ('nit', models.IntegerField()),
                ('nationality', models.CharField(max_length=255)),
            ],
        ),
    ]