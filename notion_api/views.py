from rest_framework import filters

from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import generics

from notion.models import Notion, Tag
from .serializers import NotionSerializer, TagSerializer


class NotionListAPIView(generics.ListCreateAPIView):
    queryset = Notion.objects.all()
    serializer_class = NotionSerializer
    # permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tags']
    search_fields = ['title']

class NotionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notion.objects.all()
    serializer_class = NotionSerializer


class TagListAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

