# Generated by Django 4.0.6 on 2022-07-31 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0003_tutor_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='college_app.course'),
        ),
    ]
