from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Katigoriya'
        verbose_name_plural = 'Katigoriyalar'

class Article(models.Model):
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField()
    photo = models.ImageField(blank=True,null=True,upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
