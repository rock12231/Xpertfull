# Generated by Django 3.0.2 on 2020-03-20 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20200320_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h3white', models.TextField()),
                ('para', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]