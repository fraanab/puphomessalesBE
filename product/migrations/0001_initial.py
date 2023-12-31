# Generated by Django 4.1.3 on 2023-06-29 21:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='products/')),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
