# Generated by Django 4.0.1 on 2022-01-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_auto_20210621_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
