# Generated by Django 4.1.7 on 2023-03-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0005_landingpagebeforeafter_remove_landingpage_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='BeforeAfterPage',
            field=models.ManyToManyField(to='webs.landingpagebeforeafter'),
        ),
    ]
