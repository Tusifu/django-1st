from articles.url import article_urls,slug_url
from django.urls import include, path


urlpatterns = [
    path('',include(article_urls)),
    path('',include(slug_url))

   ]