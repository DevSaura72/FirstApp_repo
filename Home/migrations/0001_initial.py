# Generated by Django 4.2.16 on 2024-10-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UDC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(max_length=50)),
                ('val1', models.CharField(max_length=50)),
                ('val2', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=800)),
                ('ParentId', models.IntegerField()),
                ('RelationId', models.IntegerField()),
                ('CreatedBy', models.IntegerField()),
                ('CreatedOn', models.DateField()),
                ('UpdatedBy', models.IntegerField()),
                ('UpdatedOn', models.DateField()),
                ('DeletedBy', models.IntegerField()),
                ('DeletedOn', models.DateField()),
                ('IsDeleted', models.BooleanField()),
            ],
        ),
    ]
