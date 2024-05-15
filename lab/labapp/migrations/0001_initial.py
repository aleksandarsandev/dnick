# Generated by Django 5.0.3 on 2024-05-14 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publishing_House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('website', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to=None)),
                ('isbn', models.CharField(max_length=15)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('dimensions', models.CharField(max_length=11)),
                ('cover_type', models.CharField(choices=[('Hard', 'Hard'), ('Soft', 'Soft')], max_length=5)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(choices=[('Romance', 'Romance'), ('Thriler', 'Thriler'), ('Biography', 'Biography'), ('Classic', 'Classic'), ('Drama', 'Drama'), ('History', 'History')], max_length=15)),
                ('publishing_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='labapp.publishing_house')),
            ],
        ),
    ]