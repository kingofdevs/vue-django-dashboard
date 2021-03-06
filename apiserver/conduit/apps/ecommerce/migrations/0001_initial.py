# Generated by Django 2.2.8 on 2020-01-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Name')),
                ('position', models.CharField(blank=True, max_length=50, verbose_name='Position')),
                ('tax', models.IntegerField(choices=[(0, '0%'), (7, '7%'), (19, '19%')], default=0, verbose_name='Tax')),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
    ]
