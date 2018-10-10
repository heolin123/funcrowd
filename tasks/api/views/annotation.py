# -*- coding: utf-8 -*-

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

from tasks.models import Item

from tasks.api.serializers.annotation import AnnotationDataSerializer
from tasks.api.serializers.dto.annotation_response import AnnotationResponseSerializer
from tasks.controllers.annotation_controller import AnnotationController


class AnnotationDetail(GenericAPIView):
    serializer_class = AnnotationDataSerializer

    def get(self, request, item_id):
        item = Item.objects.filter(id=item_id).first()
        if item:
            annotation, created = item.get_or_create_annotation(request.user)
            response = AnnotationController().process(annotation)
            serializer = AnnotationResponseSerializer(response)
            return Response(serializer.data)
        raise NotFound("No Item found for given id.")

    def post(self, request, item_id):
        item = Item.objects.filter(id=item_id).first()
        if item:
            annotation, created = item.get_or_create_annotation(request.user)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                annotation.data = serializer.data['data']
                response = AnnotationController().process(annotation)
                serializer = AnnotationResponseSerializer(response)
            else:
                raise ValidationError("Annotation data cannot be empty.")
            return Response(serializer.data)
        raise NotFound("No Item found for given id.")
