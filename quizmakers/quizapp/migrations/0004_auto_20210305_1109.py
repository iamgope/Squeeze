# Generated by Django 3.1.6 on 2021-03-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_auto_20210226_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]
