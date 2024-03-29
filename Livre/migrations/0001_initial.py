# Generated by Django 2.2.7 on 2019-11-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='')),
                ('auteur', models.CharField(default='anonymous', max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('description', models.TextField(default='Tutoriel crud Django')),
            ],
        ),
    ]
