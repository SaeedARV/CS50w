# Generated by Django 4.1 on 2022-08-20 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_alter_comments_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='imgURL',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.CharField(max_length=5000),
        ),
    ]
