# Generated by Django 3.2 on 2021-05-01 20:26

import apps.account.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='passenger', serialize=False, to='account.user')),
                ('status', models.CharField(choices=[('waiting_for_driver', 'waiting_for_driver'), ('busy', 'busy'), ('free', 'free')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('account.user',),
            managers=[
                ('objects', apps.account.managers.UserManager()),
            ],
        ),
    ]
