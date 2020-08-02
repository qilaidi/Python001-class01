from django.shortcuts import render

# Create your views here.
from .models import MovieHamilton


def movie_short(request):
    # 三星级以上
    queryset = MovieHamilton.objects.all()
    condtions = {'stars__gt': 3}
    good_comment = queryset.filter(**condtions)

    return render(request, 'result.html', locals())