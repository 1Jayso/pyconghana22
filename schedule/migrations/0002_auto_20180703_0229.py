# Generated by Django 2.0.1 on 2018-07-03 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='room',
            field=models.CharField(choices=[('Prof. Ebenezer Oduro Owusu', 'Prof. Ebenezer Oduro Owusu'), ('H. E. K Amissah Arthur Seminar Room', 'H. E. K Amissah Arthur Seminar Room'), ('The Foyer', 'The Foyer'), ('Dr. Ernest Addison Seminar Room', 'Dr. Ernest Addison Seminar Room')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='talkschedule',
            name='room',
            field=models.CharField(choices=[('Prof. Ebenezer Oduro Owusu', 'Prof. Ebenezer Oduro Owusu'), ('H. E. K Amissah Arthur Seminar Room', 'H. E. K Amissah Arthur Seminar Room'), ('The Foyer', 'The Foyer'), ('Dr. Ernest Addison Seminar Room', 'Dr. Ernest Addison Seminar Room')], default='', max_length=10),
        ),
    ]
