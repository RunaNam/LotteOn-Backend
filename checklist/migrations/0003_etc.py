# Generated by Django 2.2.10 on 2020-10-20 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20201020_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('checked', models.BooleanField()),
            ],
        ),
    ]