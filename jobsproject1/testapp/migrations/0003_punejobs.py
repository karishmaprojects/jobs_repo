# Generated by Django 4.2.6 on 2023-11-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_bngjobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='PuneJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=60)),
                ('eligibility', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
