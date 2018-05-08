from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Coin, Storage


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ('id',  'symbol', 'value')


class StorageSerializer(serializers.ModelSerializer):
    coins = CoinSerializer(many=True, read_only=True)

    class Meta:
        model = Storage
        fields = ('id',  'name', 'coins')


class UserSerializer(serializers.ModelSerializer):
    storages = StorageSerializer(Storage, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'storages',)
