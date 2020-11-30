from django.urls import path
from create_article.views import ArticleApplyView


urlpatterns = [
    path('create_article/', ArticleApplyView.as_view(), name='create_article')
]