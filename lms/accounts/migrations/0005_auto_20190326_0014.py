# Generated by Django 2.1.5 on 2019-03-26 00:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190326_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='status',
            field=models.CharField(choices=[('213', 'ALG'), ('244', 'ANG'), ('229', 'BEN'), ('267', 'BOT'), ('246', ''), ('226', 'BUR'), ('257', 'BDI'), ('237', 'CMR'), ('238', 'CPV'), ('236', 'CAF'), ('235', 'CHA'), ('269', 'COM'), ('242', 'CGO'), ('243', 'COD'), ('253', 'DJI'), ('20', 'EGY'), ('240', 'GEQ'), ('291', 'ERI'), ('251', 'ETH'), ('', ''), ('241', 'GAB'), ('220', 'GAM'), ('233', 'GHA'), ('224', 'GUI'), ('245', 'GBS'), ('225', 'CIV'), ('254', 'KEN'), ('266', 'LES'), ('231', 'LBR'), ('218', 'LBA'), ('261', 'MAD'), ('265', 'MAW'), ('223', 'MLI'), ('222', 'MTN'), ('230', 'MRI'), ('262', ''), ('212', 'MAR'), ('258', 'MOZ'), ('264', 'NAM'), ('227', 'NIG'), ('234', 'NGR'), ('262', ''), ('250', 'RWA'), ('290', None), ('239', 'STP'), ('221', 'SEN'), ('248', 'SEY'), ('232', 'SLE'), ('252', 'SOM'), ('27', 'RSA'), ('211', ''), ('249', 'SUD'), ('268', 'SWZ'), ('255', 'TAN'), ('228', 'TOG'), ('216', 'TUN'), ('256', 'UGA'), ('212', ''), ('260', 'ZAM'), ('263', 'ZIM')], default='GHA', max_length=20),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_activity',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 215887, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reg_joined',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 215818, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='department',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 215109, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_token',
            field=models.CharField(default='pbkdf2:sha256:50000$BgTcBrix$5e492daf65275533d2a40b7ae3e3a3c0d4e3f1b598f1b537a6301ca361b994e5', max_length=1000),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='adminRemarkDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 297645, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='fromDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 297801, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='toDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 297834, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 26, 0, 14, 36, 297059, tzinfo=utc), null=True),
        ),
    ]