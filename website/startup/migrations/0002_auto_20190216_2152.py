# Generated by Django 2.1.7 on 2019-02-16 21:52

from django.db import migrations, models
import django.db.models.deletion
import startup.models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Investors',
            fields=[
                ('id', models.UUIDField(default=startup.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentors',
            fields=[
                ('id', models.UUIDField(default=startup.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OfficeSpaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('company', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgressMilestones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone', models.CharField(max_length=300)),
                ('Acheived', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Startupmembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Startupprojects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateTimeField(auto_now_add=True)),
                ('progress', models.CharField(choices=[('F', 'Finished'), ('U', 'Underway'), ('N', 'Not yet begun')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Startups',
            fields=[
                ('id', models.UUIDField(default=startup.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
        migrations.AddField(
            model_name='startupprojects',
            name='_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.Startups'),
        ),
        migrations.AddField(
            model_name='progressmilestones',
            name='_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.Startups'),
        ),
        migrations.AddField(
            model_name='invested',
            name='_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.Investors'),
        ),
        migrations.AddField(
            model_name='invested',
            name='startup_invested',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.Startups'),
        ),
    ]