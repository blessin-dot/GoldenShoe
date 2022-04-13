# Generated by Django 4.0.3 on 2022-04-12 15:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_remove_project_shoe_size_project_shoe_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('order_id', models.IntegerField(default=0)),
                ('basket_quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('prodcut_id', models.CharField(max_length=500)),
                ('product_name', models.CharField(max_length=500)),
            ],
        ),
    ]
