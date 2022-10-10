from django.contrib import admin
from .models import UserModel, Cards, ShortsV2, AnswersForShortsV2, CategoriaPost, Post


admin.site.register([UserModel, Cards, ShortsV2,
                    AnswersForShortsV2, CategoriaPost, Post])
