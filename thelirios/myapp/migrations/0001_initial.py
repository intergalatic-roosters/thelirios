# Generated by Django 4.2.11 on 2024-04-27 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('amount_yield', models.FloatField(max_length=6)),
                ('cooking_time', models.IntegerField(help_text='minutes')),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('cost', models.FloatField(max_length=6)),
                ('ingredients', models.ManyToManyField(to='myapp.ingredient')),
            ],
        ),
    ]
