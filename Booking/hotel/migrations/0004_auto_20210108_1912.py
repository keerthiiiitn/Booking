# Generated by Django 3.1.4 on 2021-01-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_book_room_booked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_room',
            name='booked',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
