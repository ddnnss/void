import json
from django.http import JsonResponse
from django.shortcuts import render
from portfolio.models import PortfolioItem
from blog.models import Article
from partner.models import Partner
from .forms import *

def index(request):
    index_active = True
    all_portfolio_items = PortfolioItem.objects.all()
    all_partners = Partner.objects.all()
    try:
        latest_blog_posts = Article.objects.all().order_by('-created_at')[2]
    except:
        latest_blog_posts = Article.objects.all().order_by('-created_at')
    return render(request, 'page/index.html', locals())


def callback(request):
    request_unicode = request.body.decode('utf-8')
    request_body = json.loads(request_unicode)
    data = request.POST.copy()
    print(request_body)
    form = CallbackOrderForm(request_body)
    return_dict = {}
    if form.is_valid():
        newForm = form.save()
        return_dict['result'] = 'ok'

    else:
        return_dict['result'] = form.errors
        print(form.errors)
    return JsonResponse(return_dict)





