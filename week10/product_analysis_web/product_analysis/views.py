from django.db.models import Avg, Count
from django.shortcuts import render

# Create your views here.
from .models import ProductCleaned

STAR = {}


def qipaoshui(request):
    ## 取出数据库内容
    contents = ProductCleaned.objects.all()
    ## 评论数量
    counter = len(contents)
    ## 情感倾向
    sent_avg = f"{contents.aggregate(Avg('sentiment'))['sentiment__avg']:0.1f}"
    ## 正向数量
    plus = contents.filter(sentiment__gte=0.5).count()
    ## 负向数量
    minus = contents.filter(sentiment__lt=0.5).count()
    page_name = '气泡水'
    print(contents[0].create_time)

    return render(request, 'result.html', locals())


def login(request):
    return render(request, 'tables.html', locals())
