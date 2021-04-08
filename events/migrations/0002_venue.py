# Generated by Django 3.1.3 on 2021-04-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=520)),
                ('zip_code', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('web_address', models.URLField(max_length=120)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
    ]