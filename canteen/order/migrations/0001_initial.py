# Generated by Django 3.0.8 on 2020-09-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('room_no', models.CharField(max_length=5)),
                ('order', models.TextField()),
            ],
        ),
    ]
