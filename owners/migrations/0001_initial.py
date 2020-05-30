# Generated by Django 3.0.6 on 2020-05-19 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import owners.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_pic', models.ImageField(default='profile_pics/default.png', upload_to=owners.models.profile_pic_filename, verbose_name='Profile Picture')),
                ('email_confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
