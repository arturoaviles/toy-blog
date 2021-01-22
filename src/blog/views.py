from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, redirect
# import datetime

from .forms import ArticleForm
from .models import Writer, Article
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import WriterSerializer, ArticleSerializer
# Create your views here.


def registerView(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            create_writer(request.POST)

    context = {"form": form}
    return render(request, 'register.html', context)


def create_writer(data):
    user = User.objects.get(username=data.get("username"))
    Writer.objects.create(user=user, name=user.username, is_editor=False)


def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutView(request):
    logout(request)
    return redirect('login')


def homePageView(request):
    writer_article_count = Writer.objects.annotate(Count("written_by"))
    # count2 = Article.objects.filter(
    #    created_at__lte=datetime.datetime.today(),
    #    created_at__gt=datetime.datetime.today()-datetime.timedelta(days=30)).\
    # values('created_at').annotate(count=Count('written_by'))
    return render(request, 'dashboard.html', context={
        "website_section": "Dashboard",
        "writer_article_count": writer_article_count
    })


@login_required
def articleCreateView(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "article_detail.html", context)


@login_required
def articleDetailView(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'article_detail.html', context)


@login_required
def articleApprovalView(request):
    if request.method == "POST":
        id_ = request.POST.get('id')
        value = request.POST.get('decision')
        decision = {"approve": 1, "reject": 2}
        record = Article.objects.filter(id=id_)
        record.update(status=decision[value])
        articles_for_approval = Article.objects.filter(status=0)
        context = {"articles_for_approval": articles_for_approval}
        return render(request, "article_approval.html", context)

    username = Writer.objects.get(user=request.user)
    if username.is_editor is True:
        articles_for_approval = Article.objects.filter(status=0)
        context = {"articles_for_approval": articles_for_approval}
        return render(request, "article_approval.html", context)
    return render(request, "error.html")


@login_required
def articlesEditedView(request):
    username = Writer.objects.get(user=request.user)
    if username.is_editor is True:
        approved_and_rejected_articles = Article.objects.filter(
            Q(status=1) | Q(status=2)
        )
        context = {
            "approved_and_rejected_articles": approved_and_rejected_articles
        }
        return render(request, "articles_edited.html", context)
    return render("error.html")


class WriterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows writers to be viewed or edited.
    """
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows articles to be viewed or edited.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]
