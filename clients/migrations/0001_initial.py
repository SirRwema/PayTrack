# Generated by Django 2.2.3 on 2019-07-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('client_name', models.CharField(max_length=250)),
                ('client_phonenumber', models.CharField(max_length=15)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_location', models.CharField(max_length=50)),
            ],
        ),
    ]
