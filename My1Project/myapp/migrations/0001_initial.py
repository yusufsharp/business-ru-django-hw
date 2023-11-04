# Generated by Django 4.2.7 on 2023-11-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='myapp/static/img/profile')),
                ('name_surname', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('Парень', 'Парень'), ('Девушка', 'Девушка')], max_length=40)),
                ('birth_date', models.DateField()),
                ('telegram', models.CharField(blank=True, max_length=40, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
