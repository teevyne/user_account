# Generated by Django 3.2.6 on 2021-08-03 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_usertransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertransaction',
            name='account_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.accountuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertransaction',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
