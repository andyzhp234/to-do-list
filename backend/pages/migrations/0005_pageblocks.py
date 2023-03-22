# Generated by Django 4.1.7 on 2023-03-20 09:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_remove_pages_tasks'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageBlocks',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('block_id', models.CharField(max_length=255)),
                ('block_type', models.CharField(max_length=255)),
                ('block_data', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.pages')),
            ],
        ),
    ]