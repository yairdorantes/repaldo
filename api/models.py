from datetime import datetime
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class UserModel(AbstractUser):
    premium = models.BooleanField(default=False, verbose_name='premium')
    #username = models.CharField(max_length=100, verbose_name='User name')
    #email = models.EmailField(verbose_name='User email',unique=True)
    #password = models.CharField(max_length=128, verbose_name='password')
    # active_user=models.BooleanField(default=True)
    #USERNAME_FIELD = 'email'
    # def __str__(self):
    #    return self.username


class Cards(models.Model):
    cardTitle = models.CharField(max_length=50, verbose_name='Card title')
    cardMeaning = models.CharField(max_length=50, verbose_name='Card meaning')
    cardImage = models.ImageField(verbose_name='Card image', upload_to='cards')
    imageURL = models.URLField(
        default="http://127.0.0.1:8000/cards/", verbose_name='Image source')

    def __str__(self):
        return self.cardTitle


class ShortsV2(models.Model):
    likes = models.IntegerField(verbose_name='Likes', default=0)
    short_name = models.CharField(max_length=50, verbose_name='Short name')
    video = models.FileField(upload_to='shorts', verbose_name='VideoFile')
    short_url = models.URLField(
        default="http://127.0.0.1:8000/", verbose_name='Short URL')
    translation = models.TextField(blank=True, verbose_name='Translation')
    question = models.CharField(max_length=100, verbose_name='Question')

    def __str__(self):
        return self.short_name


class AnswersForShortsV2(models.Model):

    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No')
    )
    parent_question = models.ForeignKey(
        ShortsV2, on_delete=models.SET_NULL, default=False, null=True, related_name="answers")
    answer_text = models.CharField(
        max_length=100, verbose_name='Answer text', default="")
    is_correct = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=False)

    def __str__(self):
        return self.answer_text + " " + " - " + self.parent_question.short_name


class CategoriaPost(models.Model):
    name = models.CharField(
        max_length=100, null=False, unique=False, verbose_name='Category Post')
    color = models.CharField(
        max_length=100, verbose_name='color ategory', default='#FFFFFF')

    class meta:
        verbose_name = 'Category'
       # ordering = ['id']

    def __str__(self):
        return self.name


class Post(models.Model):
    categoria = models.ForeignKey(
        CategoriaPost, on_delete=models.CASCADE)
    image = models.FileField(upload_to="PostImage", verbose_name="Post image")
    title = models.CharField(max_length=500, verbose_name="Post title")
    intro = models.CharField(max_length=500, verbose_name="Post intro")
    content = models.TextField(blank=True, verbose_name="Post content")
    image_src = models.URLField(
        default="http://127.0.0.1:8000/", verbose_name="post image source ")
    # likes = models.IntegerField(default=0, verbose_name="post likes")
    likes = models.ManyToManyField(
        UserModel, verbose_name="Post likes", default="")

    likes_count = models.IntegerField(
        default=0, verbose_name="Post likes counter")

    def delete(self, *args, **kwargs):
        self.image.delete()
       # os.remove(os.path.join(settings.MEDIA_ROOT, self.image))
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=255)
    text = models.TextField(blank=True, verbose_name="comment")
    created_date = models.CharField(max_length=255)
    approved_comment = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.text


"""
THIS IS TO ORDER WHAT YOU WANT(IN THIS CASE POSITION_CARD VALUES)
MODELS
    class Meta:
        ordering = ["positionCard"]
"""
