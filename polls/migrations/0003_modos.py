# Generated by Django 3.1.5 on 2021-01-27 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210127_0341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo', models.CharField(max_length=20)),
            ],
        ),
    ]
