# Generated by Django 4.1.6 on 2023-02-14 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('C', 'Coloring'), ('M', 'Music'), ('N', 'Nap'), ('R', 'Reading'), ('P', 'Play'), ('W', 'Writing')], default='C', max_length=1)),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('comment', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('DoB', models.DateField()),
                ('allergies', models.CharField(max_length=100)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=5)),
                ('children', models.ManyToManyField(to='main_app.child')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feeding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did_eat', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.child')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.child')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behavior', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.child')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
