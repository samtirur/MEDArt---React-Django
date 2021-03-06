# Generated by Django 3.2.5 on 2021-07-31 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='portal',
            new_name='applicant_city',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='applicant_address1',
            new_name='applicant_email',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='title',
            new_name='applicant_name',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='applicant_address2',
            new_name='hospital_email',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='applicant_emial',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='hospital_address1',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='hospital_address2',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='hospital_emial',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='last_name',
        ),
        migrations.AddField(
            model_name='hospital',
            name='applicant_image',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_city',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_image',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='applicant_district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='applicant_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='applicant_state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='geo_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_district',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_state',
            field=models.CharField(max_length=50),
        ),
    ]
