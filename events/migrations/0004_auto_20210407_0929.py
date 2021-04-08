# Generated by Django 3.1.3 on 2021-04-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210407_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_name', models.EmailField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='attendee',
            field=models.ManyToManyField(blank=True, to='events.Profile'),
        ),
    ]