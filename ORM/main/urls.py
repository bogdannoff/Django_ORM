from django.urls import path

from main.views import *

urlpatterns = [
    path('blog_authors', BlogAuthorsView.as_view(), name='blog-authors'),
    path('blog_authors_orm', BlogAuthorsViewORM.as_view(), name='blog-authors-orm'),
]