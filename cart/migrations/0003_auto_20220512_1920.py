# Generated by Django 2.2.25 on 2022-05-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220510_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
