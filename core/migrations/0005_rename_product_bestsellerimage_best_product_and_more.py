# Generated by Django 5.1.6 on 2025-03-25 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_bestseller_image_alter_bestsellerimage_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bestsellerimage',
            old_name='product',
            new_name='best_product',
        ),
        migrations.RenameField(
            model_name='feautureproductimage',
            old_name='product',
            new_name='feauture_product',
        ),
        migrations.RenameField(
            model_name='recentproductimage',
            old_name='product',
            new_name='recent_product',
        ),
        migrations.RenameField(
            model_name='specialofferimage',
            old_name='product',
            new_name='special_product',
        ),
    ]
