# Generated by Django 3.0.5 on 2020-11-10 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20201110_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('In Door', 'In Door'), ('Out Door', 'Out Door')], max_length=255, null=True),
        ),
    ]
