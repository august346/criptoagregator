from django.conf.urls import url
from django.urls import include
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf
from .views import UserViewSet, StoragesView, CoinView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'v1/storages/', StoragesView.as_view()),
    url(r'v1/coin/', CoinView.as_view()),

]
