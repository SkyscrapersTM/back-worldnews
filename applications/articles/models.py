from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    author = models.CharField(max_length=60)
    content = RichTextField()
    urlToImage = models.URLField(max_length=255)
    publishedAt = models.DateField(
        'Publication Date', auto_now=True, auto_now_add=False)
    status = models.BooleanField("Published/No Published", default=True)

    article_category_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.title
