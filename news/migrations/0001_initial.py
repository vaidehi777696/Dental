# Generated by Django 5.0 on 2024-05-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='event_photos/')),
                ('is_past_event', models.BooleanField(default=False)),
            ],
        ),
    ]
