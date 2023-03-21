# Generated by Django 4.1.7 on 2023-03-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webs', '0013_alter_booking_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='STATUS',
            field=models.CharField(choices=[('انتظار', 'انتظار'), ('ارسل', 'ارسل')], default='انتظار', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='knew',
            field=models.CharField(choices=[('كيف عرفتنا', 'كيف عرفتنا'), ('تأمين', 'تأمين'), ('صديق ', 'صديق '), ('أسرة', 'أسرة'), ('الجيران', 'الجيران'), ('جوجل ', 'جوجل '), ('واتساب', 'واتساب'), ('سناب', 'سناب'), ('انستقرام', 'انستقرام'), ('تويتر', 'تويتر'), ('فيس بوك ', 'فيس بوك '), ('تيك توك', 'تيك توك'), ('يوتيوب ', 'يوتيوب '), ('البريد الإلكتروني', 'البريد الإلكتروني'), ('موقع', ' موقع الإلكتروني'), ('آخر', 'آخر')], default='كيف عرفتنا', max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='web',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/Doctors/photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='Name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='jobtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/Image/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='imagename',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='BeforeAfterPage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpagebeforeafter'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='DescriptionPage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpagedescription'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='PricePage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpageprice'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='QuestionsPage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpagequestions'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='ReviewsPage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpagereviews'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='imagePage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpageimage'),
        ),
        migrations.AlterField(
            model_name='landingpagebeforeafter',
            name='Description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagebeforeafter',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPageBeforeAfter/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='landingpagebeforeafter',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagedescription',
            name='Description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagedescription',
            name='Titel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landingpageimage',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPageImage/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='landingpageimage',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landingpageprice',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagequestions',
            name='answer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagequestions',
            name='question',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='landingpagereviews',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPageReviews/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='landingpagereviews',
            name='Name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='Description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/Section/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='Description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='Doctor',
            field=models.ManyToManyField(blank=True, null=True, to='webs.doctors'),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPage/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='ImageName',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='discount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='slideImage',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPage/photos/slideImage/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='slideImage1',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPage/photos/slideImage1/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='slideImage2',
            field=models.FileField(blank=True, null=True, upload_to='files/images/LandingPage/photos/slideImage2/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='servicesproperty',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='Description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='Doctor',
            field=models.ManyToManyField(blank=True, null=True, to='webs.doctors'),
        ),
        migrations.AlterField(
            model_name='web',
            name='FaviconIco',
            field=models.FileField(blank=True, null=True, upload_to='files/images/WEB/photos/FaviconIco/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='web',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to='files/images/WEB/photos/Image/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='web',
            name='Landingpage',
            field=models.ManyToManyField(blank=True, null=True, to='webs.landingpage'),
        ),
        migrations.AlterField(
            model_name='web',
            name='Title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='authorLinke',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='info',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='keywords',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='files/images/WEB/photos/logo/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='web',
            name='silderImage',
            field=models.FileField(blank=True, null=True, upload_to='files/images/WEB/photos/silderImage/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='web',
            name='slug',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]