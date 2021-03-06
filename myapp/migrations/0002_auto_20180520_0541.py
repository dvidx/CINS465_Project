# Generated by Django 2.0.2 on 2018-05-20 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_model',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket_model',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Event_Model'),
        ),
    ]
