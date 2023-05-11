from django.shortcuts import render
from article.models import Article

def index(request):
    article = Article.objects.all()
    return render(request, 'index.html', {'articles':article})