# Generated by Django 4.0.6 on 2022-08-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0005_alter_tutor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='Image',
            field=models.ImageField(default='image/tutor/default.png', upload_to='image/tutor'),
        ),
    ]
