# Generated by Django 2.2.1 on 2019-05-21 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMdiagnose', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='marks',
            field=models.CharField(blank=True, default='0', max_length=200, null=True),
        ),
    ]
