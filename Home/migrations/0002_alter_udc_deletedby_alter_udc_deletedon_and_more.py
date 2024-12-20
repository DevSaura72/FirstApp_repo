# Generated by Django 4.2.16 on 2024-10-26 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='udc',
            name='DeletedBy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='udc',
            name='DeletedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='udc',
            name='IsDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='udc',
            name='UpdatedBy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='udc',
            name='UpdatedOn',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('EmailId', models.CharField(max_length=120)),
                ('ContactNo', models.CharField(max_length=13)),
                ('Address', models.CharField(max_length=800)),
                ('CreatedBy', models.IntegerField()),
                ('CreatedOn', models.DateField()),
                ('UpdatedBy', models.IntegerField(blank=True, null=True)),
                ('UpdatedOn', models.DateField(blank=True, null=True)),
                ('DeletedBy', models.IntegerField(blank=True, null=True)),
                ('DeletedOn', models.DateField(blank=True, null=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('DepartmentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_in_department', to='Home.udc')),
                ('EmploymentTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_with_employment_type', to='Home.udc')),
                ('WorkLocationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees_in_work_location', to='Home.udc')),
            ],
        ),
    ]
