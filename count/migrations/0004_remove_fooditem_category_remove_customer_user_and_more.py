# Generated by Django 5.1.4 on 2025-01-12 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0003_auto_20211125_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userfooditem',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='userfooditem',
            name='fooditem',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='carbohydrates',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='fooditem',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='calories',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='UserFoodItem',
        ),
    ]
