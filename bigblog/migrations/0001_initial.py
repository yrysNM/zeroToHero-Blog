# Generated by Django 3.2.12 on 2022-02-15 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('like_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigblog.likes')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigblog.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2500)),
                ('date', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigblog.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigblog.user')),
            ],
        ),
    ]
