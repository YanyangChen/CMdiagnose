# Generated by Django 2.2.1 on 2019-06-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMdiagnose', '0003_auto_20190522_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responses', models.CharField(blank=True, default='nothing', max_length=2000, null=True)),
                ('properties', models.CharField(blank=True, default='nothing', max_length=2000, null=True)),
            ],
        ),
    ]
