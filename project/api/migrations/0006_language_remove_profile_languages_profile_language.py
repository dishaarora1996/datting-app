# Generated by Django 4.2.1 on 2023-06-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='languages',
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='language', to='api.language'),
        ),
    ]