import string
from rest_framework.serializers import ModelSerializer
from applications.articles.models import Article

from django.utils.html import format_html


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        # exclude = ('status','article_category_id',)

    def to_representation(self, instance):
        
        return {
            "id": instance.id,
            "title": instance.title,
            "description": instance.description,
            "author": instance.author,
            "content": instance.content.replace('\r\n',''),
            "urlToImage": instance.urlToImage,
            "publishedAt": instance.publishedAt
        }
