from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import action

from applications.articles.models import Article, Category
from applications.articles.api.serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    serializer_class = ArticleSerializer
    queryset = ArticleSerializer.Meta.model.objects.all()

    # Create a custom viewset
    @action(detail=False, methods=['get'], url_path='article-by')
    def article_by_category(self, request, pk=None):

        # get data from url parameter
        category_param = request.query_params.get('category')

        # return object with the filter to search
        category = Category.objects.get(name=category_param)

        # returns objects with the filter to search
        article = Article.objects.filter(
            article_category_id=category, status=True)

        # check if an order instance exists
        if article:

            # convert a Order object to a JSON format
            serializer = ArticleSerializer(article, many=True)

            # display orders data for the response
            return Response(serializer.data, status=status.HTTP_200_OK)

        # display status 400 for the response
        return Response({'mensaje': 'No se ha encontrado los articulos.'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = Article.objects.filter(status=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        return Response(response_list)
