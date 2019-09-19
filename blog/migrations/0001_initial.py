# Generated by Django 2.2.5 on 2019-09-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255, verbose_name='Title')),
                ('Publication_Date', models.DateTimeField()),
                ('Body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]