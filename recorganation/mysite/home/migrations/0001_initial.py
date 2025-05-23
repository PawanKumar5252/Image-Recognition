# Generated by Django 5.2.1 on 2025-05-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Category_video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=100)),
                ('c_name', models.CharField(max_length=100)),
                ('c_video_blob', models.BinaryField(default=bytes)),
                ('c_video_file', models.FileField(upload_to='videos/')),
                ('c_uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'category_video',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('sess_time', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'session',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=254)),
                ('upassword', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
