# Generated by Django 3.1.3 on 2020-11-05 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='rec_by',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='status_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='status_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='status',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
