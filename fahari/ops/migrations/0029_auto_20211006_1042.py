# Generated by Django 3.2.7 on 2021-10-06 07:42

from django.db import migrations, models
import fahari.common.models.utils


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0028_auto_20210922_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklyprogramupdate',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to=fahari.common.models.utils.get_directory, verbose_name='Attach File or Photo'),
        ),
        migrations.AddField(
            model_name='weeklyprogramupdate',
            name='description',
            field=models.TextField(default='-', verbose_name='Task description'),
        ),
        migrations.AddField(
            model_name='weeklyprogramupdate',
            name='title',
            field=models.CharField(default='Program title', max_length=200, verbose_name='Task title'),
        ),
        migrations.AlterField(
            model_name='weeklyprogramupdate',
            name='operation_area',
            field=models.CharField(choices=[('admin', 'Administration'), ('finance', 'Finance'), ('awarding', 'Awarding'), ('subgranting', 'Subgranting'), ('sii', 'Strategic Information System'), ('program', 'Program')], default='program', help_text='Task Operation Area', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='weeklyprogramupdate',
            unique_together=set(),
        ),
    ]