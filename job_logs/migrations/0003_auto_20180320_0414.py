# Generated by Django 2.0.3 on 2018-03-20 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_logs', '0002_auto_20180312_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_logs.Topic'),
        ),
    ]