from rest_framework.routers import DefaultRouter

from applications.articles.api.views import ArticleView

router = DefaultRouter()

router.register(r'top-headlines', ArticleView, basename='article')

urlpatterns = router.urls
