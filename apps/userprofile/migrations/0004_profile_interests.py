# Generated by Django 4.0.4 on 2022-05-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_alter_profile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, choices=[('Programming', 'Programming'), ('Business training', 'Business training'), ('Computer games', 'Computer games'), ('Music', 'Music'), ('Creation', 'Creation'), ('Sport', 'Sport'), ('Reading', 'Reading')], max_length=60, null=True),
        ),
    ]
