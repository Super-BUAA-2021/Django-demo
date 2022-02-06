# Generated by Django 3.2 on 2022-02-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('article', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]