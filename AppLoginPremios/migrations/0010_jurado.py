# Generated by Django 4.1.2 on 2023-02-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLoginPremios', '0009_cronograma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreJurado', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=100)),
                ('manifestacionArtistica', models.CharField(max_length=100)),
            ],
        ),
    ]