# Generated by Django 2.2.12 on 2021-10-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_events1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('field', models.CharField(max_length=250)),
            ],
        ),
    ]
