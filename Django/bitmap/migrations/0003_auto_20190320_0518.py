# Generated by Django 2.1.7 on 2019-03-20 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitmap', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userfb', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]