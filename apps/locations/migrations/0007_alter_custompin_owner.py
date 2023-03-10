# Generated by Django 4.1.5 on 2023-03-09 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0006_custompin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompin',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_pins', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
