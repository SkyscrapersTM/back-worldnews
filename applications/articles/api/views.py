from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import action

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


from applications.articles.models import Article, Category
from applications.articles.api.serializers import ArticleSerializer


class ArticleView(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    serializer_class = ArticleSerializer
    queryset = ArticleSerializer.Meta.model.objects.all()

    @swagger_auto_schema(
        operation_description="""
        Filter all articles according to their category and true status.
        Return all articles except - (article_category_id).
        """,
        manual_parameters=[openapi.Parameter(
            name="category",
            type=openapi.TYPE_STRING,
            description="The name of an article within the paginated result set",
            required=True,
            in_=openapi.IN_QUERY
        )],
        responses={200: "Success"}
    )
    # Create a custom viewset
    @ action(detail=False, methods=['get'], url_path='article-by')
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

            # set paginate to article
            page = self.paginate_queryset(article)

            # check if poage exist
            if page is not None:
                serializer = ArticleSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            # convert a article object to a JSON format
            serializer = ArticleSerializer(article, many=True)

            # display article data for the response
            return Response(serializer.data, status=status.HTTP_200_OK)

        # display status 400 for the response
        return Response({'mensaje': 'No se ha encontrado los articulos.'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        """
        List all articles that have their true state.
        Return all articles except - (article_category_id)
        """
        queryset = Article.objects.filter(status=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        return Response(response_list)
