# Generated by Django 2.1.10 on 2019-10-22 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacios', '0003_auto_20191004_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=255)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('modified_by', models.CharField(blank=True, editable=False, max_length=255)),
            ],
        ),
    ]