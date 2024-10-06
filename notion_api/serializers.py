from rest_framework.serializers import ModelSerializer

from notion.models import Notion, Tag


class NotionSerializer(ModelSerializer):

    class Meta:
        model = Notion
        fields = "__all__"

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
