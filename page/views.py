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
        # server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        # server.login(settings.YANDEX_LOGIN, settings.YANDEX_PASSWORD)
        # subject = f'Запрос обратного звонка c домена {request.domain.full_name}'
        # email_text = f'Поступил запрос на обратный звонок\n\n' \
        #              f' Номер телефона : {request_body["user_phone"]}\n' \
        #              f' Текст сообщения : {request_body["text"]}'
        # message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (settings.YANDEX_LOGIN, settings.MAIL_TO, subject, email_text)
        # server.sendmail(settings.YANDEX_LOGIN, settings.MAIL_TO, message.encode('utf-8'))
        # message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (settings.YANDEX_LOGIN, request.domain.email, subject, email_text)
        # server.sendmail(settings.YANDEX_LOGIN, request.domain.email, message.encode('utf-8'))
        # server.quit()
    else:
        return_dict['result'] = form.errors
        print(form.errors)
    return JsonResponse(return_dict)





