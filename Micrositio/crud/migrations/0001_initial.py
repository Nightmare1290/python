# Generated by Django 2.1.15 on 2020-03-31 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='concurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=50)),
                ('vigencia', models.CharField(max_length=30)),
                ('dirigido', models.CharField(max_length=40)),
                ('sublineas', models.CharField(max_length=40)),
                ('restricciones', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='promocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('imagen', models.CharField(max_length=50)),
                ('vigencia', models.CharField(max_length=30)),
                ('sublineas', models.CharField(max_length=40)),
                ('dirigido', models.CharField(max_length=40)),
                ('restricciones', models.CharField(max_length=200)),
                ('avances', models.CharField(max_length=100)),
                ('descuento', models.CharField(max_length=20)),
            ],
        ),
    ]
