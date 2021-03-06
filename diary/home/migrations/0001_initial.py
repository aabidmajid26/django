# Generated by Django 3.1.1 on 2021-01-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('residence', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('date', models.DateField()),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.people')),
            ],
        ),
    ]
