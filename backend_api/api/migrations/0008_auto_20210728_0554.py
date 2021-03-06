# Generated by Django 3.2.5 on 2021-07-28 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_hospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='emial',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='place',
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_address1',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_address2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_district',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_emial',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_state',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='first_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='geo_location',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_address1',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_address2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_district',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_emial',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_state',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='last_name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='portal',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='title',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
