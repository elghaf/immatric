# Generated by Django 3.2.3 on 2021-08-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_resident'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='parked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]