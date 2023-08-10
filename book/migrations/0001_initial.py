# Generated by Django 4.2.3 on 2023-08-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStoreModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Mystery', 'Mystery'), ('Horror', 'Horror'), ('Thriller', 'Thriller'), ('Romance', 'Romance'), ('Advancer', 'Advancer')], max_length=30)),
                ('first_pub', models.DateTimeField()),
                ('last_pub', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
