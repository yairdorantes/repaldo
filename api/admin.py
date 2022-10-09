from django.contrib import admin
from .models import UserModel, Cards, ShortsV2, AnswersForShortsV2

admin.site.register(UserModel)
admin.site.register(Cards)
admin.site.register(ShortsV2)
admin.site.register(AnswersForShortsV2)

# admin.site.register(Shorts)
# admin.site.register(SubCards)


# Register your models here.
