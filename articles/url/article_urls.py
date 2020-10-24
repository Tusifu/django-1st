from django.urls import path
from articles import views

app_name='articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.create_article, name='create'),
    # path('<slug>', views.articleDetail, name='article_detail'),
]
