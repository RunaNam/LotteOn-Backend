# Generated by Django 2.2.10 on 2020-10-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20201020_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='crossReaction',
            field=models.ManyToManyField(blank=True, to='food.CrossReaction'),
        ),
    ]
