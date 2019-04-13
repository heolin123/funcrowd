# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.api.serializers.storage import (
    StorageGetSerializer, StoragePostSerializer,
    StorageBatchPostSerializer)
from users.models.storage import Storage


class EndWorkerStorageView(GenericAPIView):

    def get(self, request, key, *args, **kwargs):
        storage = request.user.get_storage(key)
        serializer = StorageGetSerializer(storage)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, key, *args, **kwargs):
        serializer = StoragePostSerializer(data=request.data)
        if serializer.is_valid():
            storage = request.user.get_storage(key)
            storage.data = serializer.data['data']
            storage.save()
            serializer = StorageGetSerializer(storage)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EndWorkerStorageBatchView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        storages = Storage.objects.filter(user=request.user)
        serializer = StorageGetSerializer(storages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StorageBatchPostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            for value in serializer.data:
                storage = request.user.get_storage(value['key'])
                storage.data = value['data']
                storage.save()

            storages = Storage.objects.filter(user=request.user)
            serializer = StorageGetSerializer(storages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
