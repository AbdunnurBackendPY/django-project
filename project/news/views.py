from .models import Articles
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/Add.html'
    form_class = ArticlesForm
class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


@login_required
def add(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('home')
        else:
            error = 'The form was incorrect'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/Add.html', data)
