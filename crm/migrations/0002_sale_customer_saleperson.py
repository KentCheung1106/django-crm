# Generated by Django 4.1.7 on 2023-03-02 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('company', models.CharField(max_length=240)),
                ('department', models.CharField(max_length=240)),
                ('team', models.CharField(max_length=240)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'sale',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='salePerson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.sale'),
        ),
    ]
