# Generated by Django 3.2.6 on 2021-09-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0019_system_pattern'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='pattern',
            field=models.CharField(choices=[('NONE', 'None'), ('RESTROSPECTIVE_DATA_ENTRY', 'Retrospective data entry'), ('POINT_OF_CARE', 'Point of care'), ('HYBRID', 'Hybrid')], default='NONE', max_length=150),
        ),
    ]