# Generated by Django 2.0.1 on 2018-07-21 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ParentsChild', '0003_auto_20180722_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='govnId',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phoneNumber',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ticketCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]