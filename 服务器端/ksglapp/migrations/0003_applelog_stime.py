# Generated by Django 2.1.4 on 2019-10-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksglapp', '0002_auto_20191027_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='applelog',
            name='stime',
            field=models.CharField(db_column='时间', default='10-27 17:12:20', max_length=20, verbose_name='时间'),
        ),
    ]
