# Generated by Django 3.2.6 on 2021-08-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userbiography'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbiography',
            name='image',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
