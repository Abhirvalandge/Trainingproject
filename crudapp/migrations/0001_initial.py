# Generated by Django 3.2.5 on 2021-07-15 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.CharField(max_length=100)),
                ('ename', models.CharField(max_length=100)),
                ('emobile', models.CharField(max_length=100)),
                ('esal', models.CharField(max_length=100)),
            ],
        ),
    ]
