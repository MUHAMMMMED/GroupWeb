# Generated by Django 4.1.7 on 2023-03-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0017_alter_web_address_alter_web_openinghours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicesproperty',
            name='WebName',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='LandingPage',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]