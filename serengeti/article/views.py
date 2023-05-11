from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ArticleForm
from .models import Article

def home(request):
    article = Article.objects.all()
    paginator = Paginator(article, 3)
    page_number = request.GET.get("page")
    page_obg = paginator.get_page(page_number)
    return render(request, 'index.html', {'articles': article})

def new(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save(
                commit=False
            )

            article.author = request.user
            article.save()
            return redirect('article:detail', id=article.id)

    return render(request, 'new.html', {'form' : form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)

    return render(request, 'detail.html', {'article':article})

def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('article:detail', id=article.id)

    return render(request, 'edit.html', {'form' : form, 'article':article})

def destroy(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    return redirect('main:index')