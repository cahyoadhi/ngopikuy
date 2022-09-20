# Generated by Django 4.1 on 2022-09-11 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ngopikuy', '0008_alter_order_complete'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserOrder',
            new_name='Cart',
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
