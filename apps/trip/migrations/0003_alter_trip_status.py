# Generated by Django 3.2 on 2021-05-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_auto_20210502_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='status',
            field=models.CharField(choices=[('REQUESTED', 'REQUESTED'), ('STARTED', 'STARTED'), ('IN_PROGRESS', 'IN_PROGRESS'), ('COMPLETED', 'COMPLETED')], default='', max_length=11),
        ),
    ]