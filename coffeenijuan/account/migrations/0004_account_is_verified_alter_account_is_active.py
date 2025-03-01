# Generated by Django 4.0.2 on 2022-03-10 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
