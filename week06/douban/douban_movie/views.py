from django.shortcuts import render

# Create your views here.
from .models import MovieHamilton


def movie_short(request):
    # 三星级以上
    search_key = request.GET.get('search_input')
    condtions = {'stars__gt': 3}
    if search_key:
        condtions = {"shorts__contains": search_key}
    queryset = MovieHamilton.objects.all()
    good_comment = queryset.filter(**condtions)
    return render(request, 'result.html', locals())