# Generated by Django 3.1.7 on 2021-03-28 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0006_hit_service'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='hit',
            index=models.Index(fields=['service', '-start_time'], name='analytics_h_service_f4f41e_idx'),
        ),
    ]
