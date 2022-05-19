# Generated by Django 3.2.4 on 2022-04-20 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personalizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personalizado_uuid', models.UUIDField()),
                ('name_especial', models.CharField(max_length=64)),
                ('description_especial', models.TextField()),
                ('image_especial', models.URLField()),
            ],
        ),
    ]