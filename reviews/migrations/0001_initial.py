# Generated by Django 5.0.6 on 2024-05-31 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('author_name', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
