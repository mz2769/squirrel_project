# Generated by Django 2.2.7 on 2019-12-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0011_auto_20191203_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='indifferent',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='runs_from',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=2),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=20),
        ),
    ]
