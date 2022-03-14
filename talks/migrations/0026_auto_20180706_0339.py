# Generated by Django 2.0.1 on 2018-07-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0025_auto_20180706_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='talk_type',
            field=models.CharField(choices=[('-', '-'), ('Short Talk', 'Short Talk - 30 mins'), ('Long Talk', 'Long Talk - 45 mins'), ('Tutorial', 'Tutorial - 2 hours or more')], max_length=20),
        ),
    ]
