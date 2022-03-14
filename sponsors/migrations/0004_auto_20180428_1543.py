# Generated by Django 2.0.1 on 2018-04-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20180421_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[('Bronze', 'Bronze - $500'), ('Silver', 'Silver - $1000'), ('Gold', 'Gold - $2500'), ('Diamond', 'Diamond - $3500'), ('Other', 'Other'), ('Special', 'Special')], max_length=15),
        ),
    ]