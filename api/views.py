from importlib.metadata import metadata


import json
from django.views import View
from .models import Cards, UserModel, ShortsV2, AnswersForShortsV2
from rest_framework import viewsets
from .serializers import ShortsV2Serializer, AnswerShortSerializer

from django.http.response import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model
from time import sleep


User = get_user_model()


class userView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            users = list(UserModel.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                data = {'message': 'success', 'user': user}
            else:
                data = {'message': 'user not found'}
            return JsonResponse(data)
        else:
            users = list(User.objects.values())
        if len(users) > 0:
            data = {'message': 'success', 'users': users}
        else:
            data = {'message': 'user not found'}
        return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        jd = json.loads(request.body)
      #   print(jd)

        User.objects.create_user(
            username=jd['name'], email=jd['email'], password=jd['password'])
        data = {'message': 'success'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            user = User.objects.get(id=id)
            user.username = jd['name']
            user.email = jd['email']
            user.password = jd['password']
            user.save()
            data = {'message': 'success'}

        else:
            data = {'message': 'user not found'}
        return JsonResponse(data)

    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            data = {'message': 'success'}

        else:
            data = {'message': 'user not found'}
        return JsonResponse(data)


class cardView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):

        cards = list(Cards.objects.values())
        if len(cards) > 0:
            data = {'message': 'success', 'cards': cards}
        else:
            data = {'message': 'card not found'}
      #  sleep(1.3)
        return JsonResponse(data)


class shortV2View(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        shorts = list(ShortsV2.objects.values())
        if len(shorts) > 0:
            data = {'message': 'success', 'shortsV2': shorts}
        else:
            data = {'message': 'short not found'}
        return JsonResponse(data)


class shortV2Set(viewsets.ModelViewSet):
    serializer_class = ShortsV2Serializer

    def get_queryset(self):
        shorts = ShortsV2.objects.all()
        return shorts


class AnswersForShortsV2Set(viewsets.ModelViewSet):
    serializer_class = AnswerShortSerializer

    def get_queryset(self):
        answers = AnswersForShortsV2
        return answers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh'
    ]
    return Response(routes)


class userToPremium(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request, id):
        # jd = json.loads(request.body)
        user = User.objects.get(id=id)
        user.premium = True
        user.save()
        data = {'message': 'user is now premium!'}
        return JsonResponse(data)
