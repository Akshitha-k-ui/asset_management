# Generated by Django 5.1 on 2024-09-01 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_alter_managedasset_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managedasset',
            name='category_id',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='AssetIssue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_description', models.TextField()),
                ('expired_date', models.DateField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='assets.asset')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.employee')),
            ],
        ),
    ]
