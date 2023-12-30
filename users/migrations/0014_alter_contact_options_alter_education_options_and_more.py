# Generated by Django 4.2.6 on 2023-12-30 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_experience_education_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-start_date'], 'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-start_date'], 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
    ]