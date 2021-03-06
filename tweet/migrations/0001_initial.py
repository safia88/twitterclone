# Generated by Django 3.0.6 on 2020-06-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=140)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-creation_date',),
            },
        ),
    ]
