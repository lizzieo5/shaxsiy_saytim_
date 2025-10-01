from django.urls import path
from django.views.generic import DetailView

from .views import (
    ArticleListView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleCreateView,
    YonaltirishView,
)


urlpatterns = [

    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('yonaltirish/', YonaltirishView.as_view(), name='yonaltirish'),
]