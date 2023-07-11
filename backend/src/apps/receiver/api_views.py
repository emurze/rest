from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, \
    DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from taggit.models import Tag

from apps.receiver.models import Women
from apps.receiver.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from apps.receiver.serializers import WomenSerializer


# class WomenListCreate(ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenDetail(RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenDestroy(RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenModelViewSet(ModelViewSet):
    serializer_class = WomenSerializer

    def get_queryset(self):
        if pk := self.kwargs.get('pk'):
            return Women.objects.filter(pk=pk)
        else:
            return Women.objects.all()[:3]

    @action(methods=['get'], detail=True)
    def tags(self, request, pk: int | None = None) -> Response:
        if pk:
            tag = Tag.objects.get(pk=pk)
            return Response({'tag': tag.name})
        else:
            tags = Tag.objects.all()
            return Response({'tags': [tag.name for tag in tags]})

# class WomenAPIView(APIView):
#     @staticmethod
#     def get(request, *args, **kwargs):
#         if pk := kwargs.get('pk'):
#             try:
#                 instance = Women.objects.get(pk=pk)
#             except (Women.DoesNotExist, Women.MultipleObjectsReturned) as exp:
#                 raise ValidationError(exp)
#             serializer = WomenSerializer(instance)
#         else:
#             women = Women.objects.all()
#             serializer = WomenSerializer(women, many=True)
#         return Response(serializer.data)
#
#     @staticmethod
#     def post(request, *args, **kwargs):
#         if kwargs:
#             raise ValidationError('POST is not allowed.')
#
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     @staticmethod
#     def put(request, *args, **kwargs):
#         if not (pk := kwargs.get('pk')):
#             raise ValidationError('PUT is not allowed.')
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except (Women.DoesNotExist, Women.MultipleObjectsReturned) as exp:
#             raise ValidationError(exp)
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.save()
#
#         return Response(serializer.data)
#
#     @staticmethod
#     def delete(request, *args, **kwargs):
#         if not (pk := kwargs.get('pk')):
#             raise ValidationError('DELETE is not allowed.')
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except (Women.DoesNotExist, Women.MultipleObjectsReturned) as exp:
#             raise ValidationError(exp)
#
#         serializer = WomenSerializer(instance=instance)
#         serializer.delete()
#
#         return Response(serializer.data)
