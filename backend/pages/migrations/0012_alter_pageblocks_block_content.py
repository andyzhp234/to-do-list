# Generated by Django 4.1.7 on 2023-03-21 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_pageblocks_block_nextid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pageblocks',
            name='block_content',
            field=models.TextField(blank=True),
        ),
    ]
