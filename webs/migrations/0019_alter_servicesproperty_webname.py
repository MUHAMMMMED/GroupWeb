# Generated by Django 4.1.7 on 2023-03-21 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0018_servicesproperty_webname_alter_booking_landingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicesproperty',
            name='WebName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]