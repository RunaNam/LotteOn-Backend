# Generated by Django 2.2.10 on 2020-10-20 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20201021_0118'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeIng',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='division',
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='crossReaction',
            field=models.ManyToManyField(blank=True, to='food.CrossReaction'),
        ),
    ]