from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from news.models import News
from news.forms import NewsForm


def all_news(request):
    news = News.objects.all()
    context = {
        'news': news,
        'form': NewsForm()
    }
    return render(request, 'news/main_page.html', context)


@login_required(login_url='/login')
def news_info(request, id):
    news = News.objects.get(pk=id)
    context = {
        'news': news
    }
    return render(request, 'news/info_page.html', context)


@login_required(login_url='/login')
def create_news(request):
    form = NewsForm(request.POST)

    if form.is_valid():
        form.save()
    return redirect('news')
