# Generated by Django 4.1.3 on 2023-01-03 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matkul',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('matkul', models.CharField(max_length=80)),
                ('kodemk', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['matkul'],
            },
        ),
    ]
