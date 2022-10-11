
from .models import ShortsV2, AnswersForShortsV2, CategoriaPost, Post
from rest_framework import serializers


class AnswerShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswersForShortsV2
        fields = "__all__"


class ShortsV2Serializer(serializers.ModelSerializer):
    answers = AnswerShortSerializer(many=True, read_only=True)

    class Meta:
        model = ShortsV2
        fields = "__all__"
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaPost
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    categoria = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
