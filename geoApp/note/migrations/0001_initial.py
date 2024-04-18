# Generated by Django 3.1.4 on 2021-02-02 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_heading', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]