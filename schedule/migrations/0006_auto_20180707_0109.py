# Generated by Django 2.0.1 on 2018-07-07 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20180706_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='room',
            field=models.CharField(choices=[('-', '-'), ('H. E. K Amissah Arthur Seminar Room', 'H. E. K Amissah Arthur Seminar Room'), ('The Foyer', 'The Foyer'), ('Prof. Ebenezer Oduro Owusu Seminar Room', 'Prof. Ebenezer Oduro Owusu Seminar Room'), ('Dr. Ernest Addison Seminar Room', 'Dr. Ernest Addison Seminar Room')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='talkschedule',
            name='room',
            field=models.CharField(choices=[('-', '-'), ('H. E. K Amissah Arthur Seminar Room', 'H. E. K Amissah Arthur Seminar Room'), ('The Foyer', 'The Foyer'), ('Prof. Ebenezer Oduro Owusu Seminar Room', 'Prof. Ebenezer Oduro Owusu Seminar Room'), ('Dr. Ernest Addison Seminar Room', 'Dr. Ernest Addison Seminar Room')], default='', max_length=100),
        ),
    ]