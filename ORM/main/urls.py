from django.urls import path

from main.views import BlogAuthorsView

urlpatterns = [
    path('blog_authors', BlogAuthorsView.as_view(), name='blog-authors'),
]