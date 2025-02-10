from .models import Articles
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


@login_required
def add(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # Создаём объект, но не сохраняем в базу данных
            article.user = request.user  # Назначаем текущего пользователя как автора
            article.save()  # Сохраняем объект в базу данных
            return redirect('home')  # Перенаправление на главную или любую другую страницу
        else:
            error = 'The form was incorrect'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/Add.html', data)
