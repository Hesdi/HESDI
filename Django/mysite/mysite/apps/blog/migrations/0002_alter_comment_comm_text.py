# Generated by Django 4.1.2 on 2022-11-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comm_text',
            field=models.CharField(max_length=200, verbose_name='Text'),
        ),
    ]
