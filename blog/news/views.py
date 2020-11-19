from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import News

def all_news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/main_page.html', context)

@login_required(login_url='/login')
def news_info(request, id):
    news = News.objects.get(pk=id)
    context = {
        'news': news
    }
    return render(request, 'news/info_page.html', context)
