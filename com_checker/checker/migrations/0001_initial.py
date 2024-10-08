# Generated by Django 5.1 on 2024-09-21 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('work_life_balance_rating', models.FloatField()),
                ('compensation_rating', models.FloatField()),
                ('career_advancement_rating', models.FloatField()),
                ('management_relationship_rating', models.FloatField()),
                ('work_environment_rating', models.FloatField()),
                ('overall_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='company_images/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='checker.company')),
            ],
        ),
    ]
