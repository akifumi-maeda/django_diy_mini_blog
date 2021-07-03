from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.urls import reverse

class BlogAuthor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name='ユーザー')
    bio = models.TextField(max_length=400, help_text='経歴をここに記入。', verbose_name='経歴')

    class Meta:
        ordering = ['user', 'bio']
        verbose_name_plural = 'ブログ著者'

    def get_absolute_url(self):
        return reverse('blogs-by-author', args=[str(self.id)])

    def __str__(self):
        return self.user.username

from datetime import date

class Blog(models.Model):
    name = models.CharField(max_length=200, verbose_name='ブログ名')
    author = models.ForeignKey(BlogAuthor, on_delete=models.SET_NULL, null=True, verbose_name='著者')
    description = models.TextField(max_length=2000, help_text='ブログの本文をここに記入。', verbose_name='本文')
    post_date = models.DateField(default=date.today, verbose_name='投稿日')

    class Meta:
        ordering = ['-post_date']
        verbose_name_plural = 'ブログ'

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    description = models.TextField(max_length=1000, help_text='ブログへのコメントをここに記入。', verbose_name='コメント本文')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='コメント記入者')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='ブログ')
    post_date = models.DateField(auto_now_add=True, verbose_name='投稿日')

    class Meta:
        ordering = ['-post_date']
        verbose_name_plural = 'ブログコメント'

    def __str__(self):
        return self.description
