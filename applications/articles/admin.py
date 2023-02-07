from django.contrib import admin
from applications.articles.models import Category, Article
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    class Meta:
        resource_class = CategoryResource


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'author', 'article_category_id',
                    'publishedAt', 'status',)
    resource_class = ArticleResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
