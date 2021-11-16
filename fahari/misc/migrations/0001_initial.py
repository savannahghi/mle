# Generated by Django 3.2.9 on 2021-11-10 05:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fahari.common.models.base_models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0024_auto_20210919_1704'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SheetToDBMappingsMetadata',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='A descriptive name for a mapping.')),
                ('mappings_metadata', models.JSONField(default=dict, help_text='Sheet to DB mappings')),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='misc_sheettodbmappingsmetadata_related', to='common.organisation')),
            ],
            options={
                'verbose_name_plural': 'Sheet to db mappings metadata',
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
            managers=[
                ('objects', fahari.common.models.base_models.AbstractBaseManager()),
            ],
        ),
        migrations.CreateModel(
            name='StockVerificationReceiptsAdapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.UUIDField(blank=True, null=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_by', models.UUIDField(blank=True, null=True)),
                ('sheet_id', models.TextField(verbose_name='Google Spreadsheet Id')),
                ('data_sheet_name', models.CharField(help_text='The name of the sheet contain the data to be ingested.', max_length=255)),
                ('first_column', models.CharField(default='A', max_length=3)),
                ('last_column', models.CharField(max_length=3)),
                ('position', models.PositiveIntegerField(default=1, help_text='The last ingest row. The next ingest will begin at the row after this one.')),
                ('last_ingested', models.DateTimeField(blank=True, editable=False, null=True)),
                ('county', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kajiado', 'Kajiado')], max_length=65, unique=True)),
                ('field_mappings_meta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='misc.sheettodbmappingsmetadata')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='misc_stockverificationreceiptsadapter_related', to='common.organisation')),
                ('target_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.contenttype')),
            ],
            options={
                'ordering': ('-updated', '-created'),
                'abstract': False,
            },
            managers=[
                ('objects', fahari.common.models.base_models.AbstractBaseManager()),
            ],
        ),
    ]