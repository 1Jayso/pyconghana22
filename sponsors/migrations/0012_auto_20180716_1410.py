# Generated by Django 2.0.1 on 2018-07-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0011_sponsor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='category',
            field=models.CharField(choices=[('Bronze', 'Bronze - $500'), ('Silver', 'Silver - $1000'), ('Gold', 'Gold - $2500'), ('Diamond', 'Diamond - $3500'), ('Diversity', 'Diversity'), ('Special', 'Special'), ('Other', 'Other')], max_length=15),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='type',
            field=models.CharField(choices=[('C', 'Corporate Sponsor'), ('S', 'Special Sponsor'), ('D', 'Diversity'), ('I', 'Individual Sponsor')], max_length=1, verbose_name='sponsor type'),
        ),
    ]
