# Generated by Django 3.2.4 on 2021-06-30 05:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210630_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogauthor', verbose_name='著者'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(help_text='ブログの本文をここに記入。', max_length=2000, verbose_name='本文'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=200, verbose_name='ブログ名'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_date',
            field=models.DateField(default=datetime.date.today, verbose_name='投稿日'),
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='bio',
            field=models.TextField(help_text='経歴をここに記入。', max_length=400, verbose_name='経歴'),
        ),
        migrations.AlterField(
            model_name='blogauthor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogauthor', verbose_name='コメント記入者'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='ブログ'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='description',
            field=models.TextField(help_text='ブログへのコメントをここに記入。', max_length=1000, verbose_name='コメント本文'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='post_date',
            field=models.DateField(auto_now_add=True, verbose_name='投稿日'),
        ),
    ]
