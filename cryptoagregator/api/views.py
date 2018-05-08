from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coin, Storage
from .serializers import UserSerializer, CoinSerializer, StorageSerializer

from rest_framework import permissions, viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StoragesView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']

    def get(self, request):
        user = request.user
        queryset = get_list_or_404(Storage, user=user)
        return Response(StorageSerializer(queryset, many=True).data)

    def post(self, request):
        user = request.user
        storage = Storage(
            name=request.data['storage_name'],
            user=user,
        )
        storage.save()
        return Response(StorageSerializer(storage).data)

    def delete(self, requset):
        data = requset.data
        storage = get_object_or_404(Storage, pk=data['id'])
        storage.delete()
        return Response({'detail': 'Storage number {} was removed'.format(data['id'])})


class CoinView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read', 'write']

    def post(self, request):
        user = request.user
        data = request.data
        storage = get_object_or_404(Storage, pk=data['storage_id'], user=user)
        coin = Coin(
            symbol=data['symbol'],
            value=data['value'],
            storage=storage,
        )
        coin.save()
        return Response(CoinSerializer(coin).data)

    def put(self, request):
        data = request.data
        coin = get_object_or_404(Coin, pk=data['id'])
        coin.symbol = data['symbol']
        coin.value = data['value']

        coin.save()
        return Response(CoinSerializer(coin).data)

    def delete(self, requset):
        data = requset.data
        coin = get_object_or_404(Coin, pk=data['id'])
        coin.delete()
        return Response({'detail': 'Coin number {} was removed'.format(data['id'])})