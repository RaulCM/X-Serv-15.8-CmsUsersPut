# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_users_put', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='Pages',
        ),
    ]
