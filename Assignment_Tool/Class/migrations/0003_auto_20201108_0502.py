# Generated by Django 3.1.3 on 2020-11-08 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0002_auto_20201108_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='sections',
        ),
        migrations.AddField(
            model_name='section',
            name='class_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Class.class'),
        ),
    ]
