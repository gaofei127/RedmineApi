# Generated by Django 2.1 on 2018-08-20 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redmine_web', '0002_ariticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='ariticle',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=500, null=True),
        ),
    ]