# Generated by Django 4.1.5 on 2023-01-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=70)),
                ('desc', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
