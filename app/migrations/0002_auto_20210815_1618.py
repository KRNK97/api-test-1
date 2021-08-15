# Generated by Django 3.1.4 on 2021-08-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(choices=[('IND', 'India'), ('SRI', 'Sri Lanka'), ('AUS', 'Australia'), ('CHN', 'China'), ('CAN', 'Canada')], default='IND', max_length=3),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]