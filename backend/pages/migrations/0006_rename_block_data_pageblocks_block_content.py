# Generated by Django 4.1.7 on 2023-03-20 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_pageblocks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pageblocks',
            old_name='block_data',
            new_name='block_content',
        ),
    ]