# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-10 15:00
from __future__ import unicode_literals

from django.db import migrations


BACKEND_FIELD_VALUE = (
    ('email_storage', 'email_action'),
    ('no_storage', 'no_action'),
)


def forward_migration(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    FormPlugin = apps.get_model('aldryn_forms', 'FormPlugin')
    for old, new in BACKEND_FIELD_VALUE:
        FormPlugin.objects.using(db_alias).filter(action_backend=old).update(action_backend=new)


def backward_migration(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    FormPlugin = apps.get_model('aldryn_forms', 'FormPlugin')
    for old, new in BACKEND_FIELD_VALUE:
        FormPlugin.objects.using(db_alias).filter(action_backend=new).update(action_backend=old)


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_forms', '0010_auto_20171220_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formplugin',
            old_name='storage_backend',
            new_name='action_backend',
        ),

        migrations.RunPython(forward_migration, backward_migration),

    ]