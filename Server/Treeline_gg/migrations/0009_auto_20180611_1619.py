# Generated by Django 2.0.5 on 2018-06-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Treeline_gg', '0008_auto_20180611_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestpractices',
            name='id',
        ),
        migrations.AddField(
            model_name='bestpractices',
            name='event_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
    ]
