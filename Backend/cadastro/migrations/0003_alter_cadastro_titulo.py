# Generated by Django 3.2.4 on 2021-07-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20210711_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastro',
            name='titulo',
            field=models.CharField(max_length=20),
        ),
    ]
