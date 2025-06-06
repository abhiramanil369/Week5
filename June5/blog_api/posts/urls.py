from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView,PostViewSet

router=DefaultRouter()
router.register('posts',PostViewSet)

urlpatterns =[
    path('api-token-auth/',obtain_auth_token,name='api_token_auht'),
    path('register/',RegisterView.as_view(),name='register'),
    path('',include(router.urls)),
]