# Generated by Django 2.2.10 on 2021-01-29 10:58

# from django.db import migrations
# import django_admin_filter.models
# try:
#     from django.db.models import JSONField
# except ImportError:
#     from django_jsonfield_backport.models import JSONField


# class Migration(migrations.Migration):

#     dependencies = [
#         ('django_admin_filter', '0003_auto_20210125_0905'),
#     ]

#     operations = [
#         migrations.AlterField(
#             model_name='filterquery',
#             name='querydict',
#             field=JSONField(default=django_admin_filter.models.default_dict),
#         ),
#     ]

# IFNO: We just copied the migration logic from 0005_auto_20210308_2052.py back
# to this migration. The JSONField of django_jsonfield_backport does not support
# mariadb <= 10.1. So we want to get rid of it. Instead we use a self built
# json field based on a TextField.

from django.db import migrations
import django_admin_filter.models


class Migration(migrations.Migration):

    dependencies = [
        ('django_admin_filter', '0003_auto_20210125_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filterquery',
            name='querydict',
            field=django_admin_filter.models.JSONField(default=django_admin_filter.models.default_dict),
        ),
    ]
