# Generated by Django 4.2.7 on 2023-11-20 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biology', '0002_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='unitId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='biology.units'),
        ),
    ]
