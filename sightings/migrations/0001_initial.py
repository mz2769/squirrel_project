# Generated by Django 2.2.7 on 2019-11-28 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('latitude', models.DecimalField(decimal_places=2, max_digits=13)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=13)),
                ('unique_squirrel_id', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2)),
                ('date', models.DateField()),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], default=None, max_length=20)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], default=None, max_length=20)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default=None, max_length=40)),
                ('specific_location', models.CharField(default=None, max_length=200)),
                ('running', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('chasing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('climbing', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('eating', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('foraging', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('other_activities', models.CharField(default=None, max_length=200)),
                ('kuks', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('quaas', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('moans', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('tail_flags', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('tail_twitches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('approaches', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('indifferent', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
                ('runs_from', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='TRUE', max_length=20)),
            ],
        ),
    ]