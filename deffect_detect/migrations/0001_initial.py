# Generated by Django 4.0.2 on 2022-04-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_model', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='examples/')),
            ],
        ),
    ]
