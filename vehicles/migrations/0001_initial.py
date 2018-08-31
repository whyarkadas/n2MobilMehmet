# Generated by Django 2.1 on 2018-08-28 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_number', models.CharField(max_length=200)),
                ('register_date', models.CharField(max_length=80)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.Brand')),
            ],
        ),
    ]
