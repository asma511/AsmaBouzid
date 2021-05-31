# Generated by Django 3.2 on 2021-05-28 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cheveux_corps_sante_visage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='corps',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.corps'),
        ),
    ]
