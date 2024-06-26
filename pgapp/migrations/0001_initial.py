# Generated by Django 5.0.1 on 2024-04-28 21:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PG',
            fields=[
                ('PG_Code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('PG_Name', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=50)),
                ('Phn_no', models.CharField(max_length=10)),
                ('rating', models.FloatField(null=True)),
                ('description', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Registration_id', models.CharField(max_length=20)),
                ('Full_name', models.CharField(max_length=25)),
                ('Email', models.CharField(max_length=50)),
                ('Mobile_number', models.CharField(max_length=10)),
                ('sharing_person', models.CharField(max_length=25, null=True)),
                ('price_person', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PGImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sharing', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('vacancies', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('PG_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgapp.pg')),
            ],
        ),
    ]
