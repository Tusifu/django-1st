from django.urls import path
from articles import views

app_name='slug'
urlpatterns = [
    path('<slug>', views.articleDetail, name='article_detail'),
]