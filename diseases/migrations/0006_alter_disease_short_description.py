# Generated by Django 4.0.4 on 2022-05-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0005_alter_disease_display_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='short_description',
            field=models.CharField(max_length=50),
        ),
    ]
