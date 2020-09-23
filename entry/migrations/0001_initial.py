# Generated by Django 3.1.1 on 2020-09-23 07:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(4, 'Minimum 4 characters are required')])),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10, 'Enter a 10 digit mobile number'), django.core.validators.MaxLengthValidator(10)])),
                ('pic', models.ImageField(upload_to='media')),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Minimum 2 Characters are required')])),
                ('purpose', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(4, 'Minimum 4 characters are required')])),
                ('mobile', models.IntegerField(validators=[django.core.validators.MinLengthValidator(10, 'Enter a 10 digit mobile number'), django.core.validators.MaxLengthValidator(10)])),
                ('email', models.EmailField(max_length=254)),
                ('no_of_people', models.IntegerField()),
                ('in_time', models.DateField()),
                ('out_time', models.DateField(auto_now=True)),
                ('employee_to_visit', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('qrcode', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='entry.user')),
            ],
        ),
    ]
