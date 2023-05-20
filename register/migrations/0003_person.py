# Generated by Django 3.1.7 on 2021-03-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20210319_0205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Some Joe', max_length=122)),
                ('username', models.CharField(default='JoeMama', max_length=12)),
                ('password', models.CharField(max_length=50)),
                ('input_face', models.CharField(max_length=500)),
            ],
        ),
    ]
