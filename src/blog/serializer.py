from .models import Writer, Article
from rest_framework import serializers


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ['name', 'is_editor']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']
