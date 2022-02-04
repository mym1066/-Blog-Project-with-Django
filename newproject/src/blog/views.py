from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, JsonResponse, Http404
from .models import Article, Category

# Create your views here.
def home(request,page=1):
    articles_list=Article.objects.published()
    paginator = Paginator(articles_list, 3)
    #page = request.GET.get('page')
    articles = paginator.get_page(page)
        # وصل شدن به مدل و گرفتن اطلاعات و ارسال به قالب
    context = {
        "articles": articles
         
        # [:3]چندتای اخر مثلا سه تای اخر را نمایش میده
    }
    return render(request, "blog/home.html", context)


class ArticleList(ListView):
    #model=Article
    #template_name="blog/home.html"
    #context_object_name="articles"
    queryset = Article.objects.published()
    paginate_by =3

   
# def detail(request, slug):
#     context = {
#         # برای صفحاتی که در دیتا بیس نیست یا  هنوز منتشر نشده ارور 404 را نشان دهد
#         "article": get_object_or_404(Article.objects.published(), slug=slug, status="p")

#     }
#     return render(request, "blog/detail.html", context)

class ArticleDetail(DetailView):
    def get_object(self):
        slug=self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


def category(request , slug,page= 1):
    category= get_object_or_404(Category, slug=slug, status=True)
    articles_list = category.articles.published()
    paginator = Paginator(articles_list, 5)
    articles = paginator.get_page(page)
    context = {
        "category":category ,
        "articles":articles

    }
    return render(request, "blog/category.html", context)
class CategoryList(ListView):
    paginate_by =3
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category']=category
        return context


class AuthorList(ListView):
    paginate_by =3
    template_name = 'blog/author_list.html'

    def get_queryset(self):
        global author
        username=self.kwargs.get('username')
        author=get_object_or_404(User, username=username)
        return author.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author']=author
        return context