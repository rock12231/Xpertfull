# Generated by Django 3.0.2 on 2020-03-06 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h3white', models.TextField()),
                ('h1white', models.TextField()),
                ('h1yellow', models.TextField()),
                ('para', models.TextField()),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
