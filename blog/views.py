from django.shortcuts import render, get_object_or_404
from .models import *
def all_articles(request):
    all_types = ArticleType.objects.all()
    all_articles = Article.objects.all().order_by('-created_at')
    try:
        top2_articles = all_articles[:2]
        showed_articles = all_articles.exclude(id__in=top2_articles)[:9]
        hidden_articles = all_articles.exclude(id__in=top2_articles).exclude(id__in=showed_articles)

    except:
        showed_articles = all_articles
    return render(request, 'page/articles.html', locals())

def article(request,article_slug):
    article = get_object_or_404(Article, name_slug=article_slug)
    try:
        all_articles = Article.objects.all().order_by('-created_at').exclude(id=article.id)[:9]
    except:
        all_articles = Article.objects.all().order_by('-created_at').exclude(id=article.id)
    return render(request, 'page/article.html', locals())