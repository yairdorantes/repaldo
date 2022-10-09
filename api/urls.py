from rest_framework_simplejwt.views import (

    TokenRefreshView,
)
from xml.etree.ElementInclude import include
from django.urls import path, include


from .views import userView, cardView, getRoutes, MyTokenObtainPairView, userToPremium, shortV2Set, shortV2View

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('shortsetV2', shortV2Set, basename="shortV2Set")

urlpatterns = [
    path('users/', userView.as_view(), name='users_list'),
    path('users/<int:id>', userView.as_view(), name='users_process'),
    path('cards/', cardView.as_view(), name='cards_list'),
    # path('shorts/', shortView.as_view(), name='shorts_list'),
    path('shortsV2/', shortV2View.as_view(), name='shorts_list'),

    path('routes/', getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('makepremium/<int:id>', userToPremium.as_view(), name='user_to_premium'),
    path('', include(router.urls)),
]
