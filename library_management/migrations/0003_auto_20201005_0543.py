# Generated by Django 3.1.2 on 2020-10-05 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_management', '0002_auto_20201005_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcollection',
            name='books',
            field=models.ManyToManyField(related_name='collection', to='library_management.Book'),
        ),
    ]