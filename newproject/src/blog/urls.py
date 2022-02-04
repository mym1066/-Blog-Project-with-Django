from django.urls import path
from .views import ArticleList, ArticleDetail, CategoryList, AuthorList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('page/<int:page>', ArticleList, name="home"),
    path('article/<slug:slug>', ArticleDetail.as_view(), name="detail"),
    path('category/<slug:slug>', CategoryList.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>',
         CategoryList.as_view(), name="category"),
    path('author/<slug:username>', AuthorList.as_view(), name="author"),
    path('author/<slug:username>/page/<int:page>',
         AuthorList.as_view(), name="author")


]
