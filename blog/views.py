from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Category, Article, Comment
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import UserLogin, UserRegister, CommentForm, ArticleForm
from django.urls import reverse_lazy
from django.db.models import Q


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()
    context = {
        'categories': categories,
        'title': 'Birinchi sayt',
        'articles': articles,
    }
    return render(request, 'blog/index.html', context)

def category_by(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    articles = Article.objects.filter(category=category)
    context = {
        'categories': categories,
        'title': category.title,
        'articles': articles
    }
    return render(request, "blog/index.html", context)

def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        "article": article,
        "title": article.title[:20]
    }
    return render(request, "blog/article_detail.html", context)


def profile(request):
    context = {
        'title':'Profile'
    }
    return render(request, "blog/profile.html", context)




class ArticleDetail(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['title'] = article.title
        context['comments'] = Comment.objects.filter(article=article)
        context['comment_form'] = CommentForm()
        return context


class AddArticle(CreateView):
    model = Article
    template_name = 'blog/add_article.html'
    form_class = ArticleForm


def user_login(request):
    if request.method =='POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = UserLogin()
    context = {
        'form': form,
        'title': 'Krish'
    }
    return render(request, 'blog/login_form.html', context)

def user_logaut(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserRegister(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = UserRegister()
    context = {
        'title':"Ro'yxatdan o'tish",
        'form':form
    }
    return render(request, 'blog/register.html', context)


def save_comment(requests, pk):
    form = CommentForm(data=requests.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = requests.user
        article = Article.objects.get(pk=pk)
        comment.article = article
        comment.save()
    else:
        pass
    return redirect('article_detail', pk)

class EditArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'




class DeleteArticle(DeleteView):
    model = Article
    success_url = reverse_lazy('index')
    context_object_name = 'article'


def search(request):
    word = request.GET.get('q')
    articles = Article.objects.filter(Q(title__icontains=word)|Q(content__icontains=word))
    context = {
        'articles': articles,
        'title': 'Qidirish'
    }
    return render(request, 'blog/index.html', context)