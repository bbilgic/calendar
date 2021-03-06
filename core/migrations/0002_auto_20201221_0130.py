# Generated by Django 3.0.4 on 2020-12-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_notificate',
            field=models.BooleanField(default=False, verbose_name='Bildirildi mi?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_ok',
            field=models.BooleanField(default=False, verbose_name='Onaylandı mı ?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_visit',
            field=models.BooleanField(default=False, verbose_name='Ziyaret edildi mi?'),
        ),
    ]
